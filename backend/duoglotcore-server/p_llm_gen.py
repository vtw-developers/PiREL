'''
TERMS
- TSP - Two source programs. Two programs in source language generated
  by filling in a template.
'''


import logging
import openai
import os
import json
import re
from typing import List, Tuple, Dict
from pathlib import Path
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages.base import BaseMessage
import langchain_core.load.dump
import ast_parse
import p_data_structures as pds
import p_utils
import p_consts
import p_llm_templates
import p_llm_val


logger = logging.getLogger(__name__)


class TemplateSimplificationRetryLimitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TSPGenerationRetryLimitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SP1TranslationRetryLimitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SP2TranslationRetryLimitException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ZeroTranslationPairsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def get_openai_credentials(**kwargs) -> Tuple[str, str]:
  env_fname = '.env.json'
  assert os.path.exists(env_fname), f'Create a "{env_fname}" file with necessary environment variables'
  env_dict = p_utils.read_json(env_fname)
  try:
    openai_api_key = env_dict['OPENAI_API_KEY']
    openai_organization = env_dict['OPENAI_ORGANIZATION']
    return openai_api_key, openai_organization
  except KeyError as err:
    _subject_name = kwargs['subject_name']
    msg = f'{_subject_name} An environment variable "{err}" must be set.'
    logger.critical(msg)
    raise RuntimeError(msg) from err


def generate_code_blocks(messages: List[BaseMessage], **kwargs) -> List[str]:
  '''
  Given a list of messages, prompt an LLM and extract all code blocks in its raw response
  '''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Starting to generate code blocks')
  raw_response = query_llm(messages, **kwargs)
  code_blocks = extract_code_blocks(raw_response, **kwargs)
  logger.debug(f'{_subject_name} Generated {len(code_blocks)} code blocks')
  return code_blocks

def query_llm(messages: List[BaseMessage], **kwargs) -> str:
  ''''''
  openai_api_key, openai_organization = get_openai_credentials(**kwargs)
  request_timeout = kwargs.get('request_timeout', p_consts.LLM_DEFAULT_REQUEST_TIMEOUT)
  max_retries = kwargs.get('max_retries', p_consts.LLM_DEFAULT_MAX_RETRIES)
  model_name = kwargs.get('model_name', p_consts.LLM_DEFAULT_MODEL_NAME)
  temperature = kwargs.get('temperature', p_consts.LLM_DEFAULT_TEMPERATURE)
  num_completions = kwargs.get('num_completions', p_consts.LLM_DEFAULT_NUM_COMPLETIONS)
  max_tokens = kwargs.get('max_tokens', p_consts.LLM_DEFAULT_MAX_TOKENS)

  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Making a query to LLM')
  logger.debug(
    f'{_subject_name} Model parameters: temperature={temperature}, model_name={model_name}, max_tokens={max_tokens}, '
    f'num_completions={num_completions}, request_timeout={request_timeout}, max_retries={max_retries}'
  )

  chatgpt = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_organization=openai_organization,
    request_timeout=request_timeout,
    max_retries=max_retries,
    n=num_completions,
    model_name=model_name,
    temperature=temperature,
    max_tokens=max_tokens
  )
  chat_result = chatgpt._generate(messages)
  raw_content = ''
  for i, generation in enumerate(chat_result.generations):
    raw_content += f'GENERATION {i}:\n'
    raw_content += generation.text
    raw_content += '\n\n'
  p_utils.log_file_time(f'{_subject_name}_llm-raw-response-{temperature}.md', raw_content)
  return raw_content

def _pre_process_raw_response(raw_response: str) -> str:
  lines = [line for line in raw_response.split('\n')]
  # 1. strip trailing whitespace characters at each line
  lines = [line.rstrip() for line in lines]
  # 2. strip leading whitespace characters at lines beginning with ```
  lines = [line.lstrip() if line.lstrip().startswith('```') else line for line in lines]
  return '\n'.join(lines)

def extract_code_blocks(raw_response: str, **kwargs) -> List[str]:
  ''''''
  raw_response = _pre_process_raw_response(raw_response)
  code_block_re = re.compile(r'^```(\w+)?\n(.*?)```$', re.DOTALL | re.MULTILINE)
  matches = re.finditer(code_block_re, raw_response)
  code_blocks = [m.group(2).strip() for m in matches]
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Extracted {len(code_blocks)} code blocks from raw LLM response')
  return code_blocks


def langchain_msgs_to_md(messages: List[BaseMessage]) -> str:
  ''''''
  result_md = ''
  for msg in messages:
    result_md += f'# {msg.type}\n\n{msg.content}\n\n\n'
  return result_md.strip()

def create_messages_simplification(src_lang: str, template: str, num_variants: int, **kwargs):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Creating messages for template simplification')
  messages = p_llm_templates.TEMPLATE_SIMPLIFICATION.format_messages(
    language=p_consts.LANG_DICT[src_lang],
    template=template,
    num_variants=num_variants
  )
  p_utils.log_file_time(f'{_subject_name}_messages-simplification.md', langchain_msgs_to_md(messages))
  return messages

def create_messages_generation(src_lang: str, template_dict: dict, **kwargs):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Creating messages for generation')
  if template_dict['is_insert_secret_fn']:
    messages = p_llm_templates.TEMPLATE_GENERATION_HAS_SECRET.format_messages(
      language=p_consts.LANG_DICT[src_lang],
      template=template_dict['template'],
      num_variants=p_consts.GENERATION_NUM_VARIANTS_IN_RESPONSE,
      secret_fn_invocation=p_consts.GENERIC_SECRET_FN_INVOCATION
    )
  else:
    messages = p_llm_templates.TEMPLATE_GENERATION_NO_SECRET.format_messages(
      language=p_consts.LANG_DICT[src_lang],
      template=template_dict['template'],
      num_variants=p_consts.GENERATION_NUM_VARIANTS_IN_RESPONSE
    )
  p_utils.log_file_time(f'{_subject_name}_messages-generation.md', langchain_msgs_to_md(messages))
  return messages

def create_messages_translation_direct_trans(program_to_translate: str, src_lang: str, tar_lang: str, **kwargs):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Creating messages for translation (direct translation)')
  messages = p_llm_templates.TEMPLATE_TRANSLATION_DIRECT_TRANS.format_messages(
    src_language=p_consts.LANG_DICT[src_lang],
    tar_language=p_consts.LANG_DICT[tar_lang],
    program_to_translate=program_to_translate
  )
  p_utils.log_file_time(f'{_subject_name}_messages-translation-direct-trans.md', langchain_msgs_to_md(messages))
  return messages

def create_messages_translation_partial_program(
  src_lang: str,
  tar_lang: str,
  snippet_to_translate: str,
  snippet_context: str,
  partial_program: str,
  variable_to_replace: str,
  **kwargs
):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Creating messages for translation of (partial program)')
  messages = p_llm_templates.TEMPLATE_TRANSLATION_PARTIAL_PROGRAM.format_messages(
    src_language=p_consts.LANG_DICT[src_lang],
    tar_language=p_consts.LANG_DICT[tar_lang],
    snippet_to_translate=snippet_to_translate,
    snippet_context=snippet_context,
    partial_program=partial_program,
    variable_to_replace=variable_to_replace
  )
  p_utils.log_file_time(f'{_subject_name}_messages-translation-partial-program.md', langchain_msgs_to_md(messages))
  return messages

def create_messages_translation_trans_similar(
  sp1: str,
  tp1: str,
  sp2: str,
  src_lang: str,
  tar_lang: str,
  **kwargs
):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Creating messages for translation (translate similar)')
  messages = p_llm_templates.TEMPLATE_TRANSLATION_TRANS_SIMILAR.format_messages(
    src_language=p_consts.LANG_DICT[src_lang],
    tar_language=p_consts.LANG_DICT[tar_lang],
    sp1=sp1,
    tp1=tp1,
    sp2=sp2
  )
  p_utils.log_file_time(f'{_subject_name}_messages-translation-trans-similar.md', langchain_msgs_to_md(messages))
  return messages


def simplify_template(src_lang: str, template_dict: dict, **kwargs) -> dict:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting template simplification')

  return_dict = {
    'simplified_template': None,
    'simplified_template_origin': None
  }

  # no context nodes that need to be simplified
  if len(template_dict['templatized_node_ids_context']) == 0:
    logger.info(f'{_subject_name} Template does not need simplification.')
    return_dict['simplified_template'] = template_dict['template_context_str_replace']
    return_dict['simplified_template_origin'] = template_dict['template_origin']
    return return_dict

  llm_temp = p_consts.GENERATION_START_TEMPERATURE
  all_raw_code_blocks = []
  retry_count = 0
  messages = create_messages_simplification(
    src_lang,
    template_dict['template_context_simplification'],
    p_consts.GENERATION_NUM_VARIANTS_IN_RESPONSE,
    **kwargs
  )

  while True:
    kwargs['temperature'] = llm_temp
    raw_code_blocks = generate_code_blocks(messages, **kwargs)
    all_raw_code_blocks.extend(raw_code_blocks)
    p_utils.log_json_time(f'{_subject_name}_simplified-template-candidates-code-blocks.json', all_raw_code_blocks)

    val_result_dict = p_llm_val.val_simplified_template_candidates(
      src_lang,
      template_dict['template_origin'],
      template_dict['templatized_node_ids_context'],
      all_raw_code_blocks,
      **kwargs
    )
    p_utils.log_json_time(f'{_subject_name}_simplification-val-{llm_temp}.json', val_result_dict)

    simplified_template = val_result_dict['simplified_template']
    templatized_node_texts = val_result_dict['templatized_node_texts']

    if simplified_template is not None:
      logger.info(f'{_subject_name} Template simplification is successful')
      template_context_str_replace: str = template_dict['template_context_str_replace']
      for templ_node_text in templatized_node_texts:
        template_context_str_replace = template_context_str_replace.replace(p_consts.CONTEXT_PH_TEXT, templ_node_text, 1)
      return_dict['simplified_template'] = template_context_str_replace
      return_dict['simplified_template_origin'] = simplified_template
      return return_dict

    logger.warning(f'{_subject_name} Template simplification is not successful. Trying one more time.')
    retry_count += 1
    llm_temp += p_consts.GENERATION_TEMPERATURE_INCREMENT
    llm_temp = round(llm_temp, p_consts.GENERATION_TEMPERATURE_ROUND_DIGITS)

    if retry_count > p_consts.SIMPLIFICATION_MAX_RETRIES:
      logger.critical(f'{_subject_name} Could not simplify the template. Reached retry limit.')
      raise TemplateSimplificationRetryLimitException

def generate_tsp(src_lang: str, template_dict: dict, **kwargs):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting two source program generation')
  template_origin = template_dict['template_origin']
  templatized_node_ids = template_dict['templatized_node_ids']
  is_insert_secret_fn = template_dict['is_insert_secret_fn']

  llm_temp = p_consts.GENERATION_START_TEMPERATURE
  all_raw_code_blocks = []
  retry_count = 0
  min_penalty = 1e100  # min penalty -> best program pair

  while True:
    messages = create_messages_generation(src_lang, template_dict, **kwargs)
    try:
      kwargs['temperature'] = llm_temp
      raw_code_blocks = generate_code_blocks(messages, **kwargs)
    except openai.InternalServerError as err:
      msg = f'{_subject_name} Failed to generate TSP from template:\n{template_dict["template"]}\ntemplate origin:\n{template_dict["template_origin"]}'
      logger.error(msg)
      runtime_err = RuntimeError(msg)
      raise runtime_err from err
    all_raw_code_blocks.extend(raw_code_blocks)
    p_utils.log_json_time(f'{_subject_name}_code-blocks-raw-{llm_temp}.json', all_raw_code_blocks)

    val_result_dict = p_llm_val.val_tsp_candidates(
      src_lang,
      template_origin,
      templatized_node_ids,
      all_raw_code_blocks,
      is_insert_secret_fn,
      **kwargs
    )
    p_utils.log_json_time(f'{_subject_name}_code-blocks-val-{llm_temp}.json', val_result_dict)

    if not val_result_dict['success']:
      logger.info(f'{_subject_name} "Two Source Programs" generation is not successful. Trying one more time.')
      retry_count += 1
      if retry_count > p_consts.GENERATION_TWO_SRC_PROGRAMS_MAX_RETRIES:
        msg = f'{_subject_name} "Two Source Programs" generation is not successful. Reached retry limit.'
        msg += f'\ntemplate:\n{template_dict["template"]}\ntemplate_origin:\n{template_dict["template_origin"]}'
        msg += f'\nlatest temperature: {llm_temp}'
        logger.critical(msg)
        raise TSPGenerationRetryLimitException(msg)
      llm_temp += p_consts.GENERATION_TEMPERATURE_INCREMENT
      llm_temp = round(llm_temp, p_consts.GENERATION_TEMPERATURE_ROUND_DIGITS)
      continue  # next iteration

    # TSP generation is successful
    logger.info(f'{_subject_name} "Two Source Programs" generation is successful. min_penalties={val_result_dict["min_penalties"]}')

    # can we improve min penalty?
    cur_min_pen = min(val_result_dict['min_penalties'].values())
    if cur_min_pen < min_penalty:
      logger.debug(f'{_subject_name} Updating min_penalty from {min_penalty} to {cur_min_pen}. Trying to improve min_penalty.')
      min_penalty = cur_min_pen
      continue  # next iteration

    # TSP generation is successful, min penalty can no longer be improved
    logger.debug(f'{_subject_name} "Two Source Programs" generation is complete. No longer can improve min_penalty.')
    program_pairs, templatized_nodes_replace_dot_w_star_flags = _get_best_n_tsps(
      val_result_dict['valid_tsp_lists_sorted'],
      val_result_dict['num_candidate_tsps_filtered']
    )
    return {
      'program_pairs': program_pairs,
      'templatized_nodes_replace_dot_w_star_flags': templatized_nodes_replace_dot_w_star_flags
    }

def _get_best_n_tsps(valid_tsp_lists_sorted: Dict[str, list], best_n: int) -> Tuple[list, list]:
  '''
  Given lists of valid TSPs per configuration, sorted by penalty (best appear first),
  choose best_n unique TSPs from each list, where uniqueness criteria is tree encoding.
  POST: len(final_TSPs_list) == best_n * len(configs)
  '''
  # objects to return
  program_pairs = []
  templatized_nodes_replace_dot_w_star_flags = []

  # use encodings to check for uniqueness
  encodings_set = []
  # for each config: index pointers in valid_tsp_lists_sorted[config]
  idxs = {_config: 0 for _config in p_consts.PENALTY_COEFS_DICT}
  # for each config: is iteration over?
  list_done = {_config: False for _config in p_consts.PENALTY_COEFS_DICT}

  while True:
    added = False
    for config in p_consts.PENALTY_COEFS_DICT:
      if idxs[config] < len(valid_tsp_lists_sorted[config]):
        ith_best_tsp = valid_tsp_lists_sorted[config][idxs[config]]
        tsp_tree_encoding = tuple(sorted([ith_best_tsp['sp1_encoding'], ith_best_tsp['sp2_encoding']]))
        if tsp_tree_encoding not in encodings_set:
          encodings_set.append(tsp_tree_encoding)
          program_pairs.append((ith_best_tsp['sp1'], ith_best_tsp['sp2']))
          templatized_nodes_replace_dot_w_star_flags.append(ith_best_tsp['templatized_nodes_replace_dot_w_star_flags'])
          added = True
        idxs[config] += 1
      else:
        list_done[config] = True
    if len(program_pairs) >= min(best_n, p_consts.TSP_BEST_N_PER_CONFIG) * len(p_consts.PENALTY_COEFS_DICT) or (not added and all(list_done.values())):
      break
  return program_pairs, templatized_nodes_replace_dot_w_star_flags


def _extract_snippet(program: str, lang: str, node_path: List[int]) -> str:
  '''
  Extract a snippet from `program` under `node_path`
  '''
  program_ast_text, _ = ast_parse.parse_text_dbg(program, lang, keep_text=True)
  program_tree = pds.PirelTree(program_ast_text)
  context_node = program_tree.get_root_node().get_children()[0]
  problematic_node = context_node.get_child_by_path(node_path)
  snippet = problematic_node.get_text().strip()
  return snippet

def _is_context_empty(template_dict: dict) -> bool:
  ''''''
  # TODO template_dict['contexts'] is a list of contexts. Which one to consider?
  return len(template_dict['contexts'][0]['source_context']['siblings']) == 0 and \
    len(template_dict['contexts'][0]['source_context']['parents']) == 0 and \
    len(template_dict['contexts'][0]['target_context']['siblings']) == 0 and \
    len(template_dict['contexts'][0]['target_context']['parents']) == 0


def translate_sp1(
  sp1: str,
  src_lang: str,
  tar_lang: str,
  template_dict: dict,
  **kwargs
) -> List[Dict[str, str]]:
  '''
  return candidate translations of SP1 in the form
  [
    {
      source: SP1,
      target: TP1_cand1
    }, ...
  ]
  '''
  if _is_context_empty(template_dict):
    return _translate_sp1_direct_trans(sp1, src_lang, tar_lang, template_dict, **kwargs)
  else:
    return _translate_sp1_partial_program(sp1, src_lang, tar_lang, template_dict, **kwargs)

def _translate_sp1_direct_trans(
  sp1: str,
  src_lang: str,
  tar_lang: str,
  template_dict: dict,
  **kwargs
) -> List[Dict[str, str]]:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting SP1 translation (direct translation)\n{sp1}')
  retry_count = 0
  while True:
    messages = create_messages_translation_direct_trans(sp1, src_lang, tar_lang, **kwargs)
    kwargs['num_completions'] = 1
    tp1_cands = generate_code_blocks(messages, **kwargs)
    p_utils.log_json_time(f'{_subject_name}_tp1-candindates-direct-trans.json', tp1_cands)
    sp1_tp1_cands = [{'source': sp1, 'target': tp1_cand} for tp1_cand in tp1_cands]
    val_result_dict = p_llm_val.val_sp1_tp1_candidates(sp1_tp1_cands, template_dict['contexts'], src_lang, tar_lang, **kwargs)
    p_utils.log_json_time(f'{_subject_name}_translation-val-result-sp1-direct-trans.json', val_result_dict)
    if val_result_dict['success']:
      return val_result_dict['good_program_pairs']
    else:
      retry_count += 1
      # potentially provide negative examples (translations that didn't work) to guide the translation
    if retry_count == p_consts.TRANSLATION_SP1_MAX_RETRIES:
      raise SP1TranslationRetryLimitException

def _translate_sp1_partial_program(
  sp1: str,
  src_lang: str,
  tar_lang: str,
  template_dict: dict,
  **kwargs
) -> List[Dict[str, str]]:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting SP1 translation (partial program)\n{sp1}')
  retry_count = 0
  while True:
    snippet_to_translate = _extract_snippet(sp1, src_lang, template_dict['problematic_node_path'])
    messages = create_messages_translation_partial_program(
      src_lang=src_lang,
      tar_lang=tar_lang,
      snippet_to_translate=snippet_to_translate,
      snippet_context=sp1,
      partial_program=template_dict['partial_program'],
      variable_to_replace=p_consts.PAR_PROG_PROB_NODE_REPLACE,
      **kwargs
    )
    kwargs['num_completions'] = 1
    tp1_cands = generate_code_blocks(messages, **kwargs)
    p_utils.log_json_time(f'{_subject_name}_tp1-candindates-partial-program.json', tp1_cands)
    sp1_tp1_cands = [{'source': sp1, 'target': tp1_cand} for tp1_cand in tp1_cands]
    val_result_dict = p_llm_val.val_sp1_tp1_candidates(sp1_tp1_cands, template_dict['contexts'], src_lang, tar_lang, **kwargs)
    p_utils.log_json_time(f'{_subject_name}_translation-val-result-sp1-partial-program.json', val_result_dict)
    if val_result_dict['success']:
      return val_result_dict['good_program_pairs']
    else:
      retry_count += 1
      # potentially provide negative examples (translations that didn't work) to guide the translation
    if retry_count == p_consts.TRANSLATION_SP1_MAX_RETRIES:
      raise SP1TranslationRetryLimitException


def translate_sp2(
  sp2: str,
  src_lang: str,
  tar_lang: str,
  sp1_tp1_cands: List[dict],
  template_dict: dict,
  **kwargs
) -> List[List[Dict[str, str]]]:
  '''
  return candidate translation pairs in the form
  [
    [
      {
        "source": "midVal1 = list1[idx] if nums1 else None",
        "target": "midVal1 = (i + Math.floor(k / 2)) - 1 < m ? list1[idx] : Infinity;"
      },
      {
        "source": "midVal1 = False[None] if nums1 else None",
        "target": "midVal1 = (i + Math.floor(k / 2)) - 1 < m ? false[null] : Infinity;"
      }
    ]
  ]
  '''
  if _is_context_empty(template_dict):
    return _translate_sp2_trans_similar(sp2, src_lang, tar_lang, sp1_tp1_cands, template_dict, **kwargs)
  else:
    return _translate_sp2_partial_program(sp2, src_lang, tar_lang, sp1_tp1_cands, template_dict, **kwargs)

def _translate_sp2_trans_similar(
  sp2: str,
  src_lang: str,
  tar_lang: str,
  sp1_tp1_cands: List[dict],
  template_dict: dict,
  **kwargs
) -> List[List[Dict[str, str]]]:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting SP2 translation (translate similar)\n{sp2}')
  translation_pairs = []
  for sp1_tp1_cand in sp1_tp1_cands:
    sp1 = sp1_tp1_cand['source']
    tp1_cand = sp1_tp1_cand['target']
    retry_count = 0
    while retry_count < p_consts.TRANSLATION_SP2_MAX_RETRIES:
      messages = create_messages_translation_trans_similar(sp1, tp1_cand, sp2, src_lang, tar_lang, **kwargs)
      kwargs['num_completions'] = 1
      tp2_cands = generate_code_blocks(messages, **kwargs)
      p_utils.log_json_time(f'{_subject_name}_tp2-candindates-trans-similar.json', tp2_cands)
      val_result_dict = p_llm_val.val_translation_pair_candidates(sp1, sp2, tp1_cand, tp2_cands, template_dict['contexts'], src_lang, tar_lang, **kwargs)
      p_utils.log_json_time(f'{_subject_name}_translation-val-result-sp2-trans-similar.json', val_result_dict)
      if val_result_dict['success']:
        logger.info(f'{_subject_name} Successfully generated at least one translation pair')
        translation_pairs.extend(val_result_dict['translation_pairs'])
        break
      logger.warning(f'{_subject_name} Could not generate a translation pair. Trying one more time.')
      retry_count += 1
  if len(translation_pairs) == 0:
    msg = f'{_subject_name} Could not generate any translation pairs in retry limit.'
    logger.critical(msg)
    raise ZeroTranslationPairsException(msg)
  return translation_pairs

def _translate_sp2_partial_program(
  sp2: str,
  src_lang: str,
  tar_lang: str,
  sp1_tp1_cands: List[dict],
  template_dict: dict,
  **kwargs
) -> List[List[Dict[str, str]]]:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting SP2 translation (partial program)\n{sp2}')
  translation_pairs = []
  for sp1_tp1_cand in sp1_tp1_cands:
    sp1 = sp1_tp1_cand['source']
    tp1_cand = sp1_tp1_cand['target']
    retry_count = 0
    while retry_count < p_consts.TRANSLATION_SP2_MAX_RETRIES:
      snippet_to_translate = _extract_snippet(sp2, src_lang, template_dict['problematic_node_path'])
      messages = create_messages_translation_partial_program(
        src_lang=src_lang,
        tar_lang=tar_lang,
        snippet_to_translate=snippet_to_translate,
        snippet_context=sp2,
        partial_program=template_dict['partial_program'],
        variable_to_replace=p_consts.PAR_PROG_PROB_NODE_REPLACE,
        **kwargs
      )
      kwargs['num_completions'] = 1
      tp2_cands = generate_code_blocks(messages, **kwargs)
      p_utils.log_json_time(f'{_subject_name}_tp2-candindates-partial-program.json', tp2_cands)
      val_result_dict = p_llm_val.val_translation_pair_candidates(sp1, sp2, tp1_cand, tp2_cands, template_dict['contexts'], src_lang, tar_lang, **kwargs)
      p_utils.log_json_time(f'{_subject_name}_translation-val-result-sp2-partial-program.json', val_result_dict)
      if val_result_dict['success']:
        logger.info(f'{_subject_name} Successfully generated at least one translation pair')
        translation_pairs.extend(val_result_dict['translation_pairs'])
        break
      logger.warning(f'{_subject_name} Could not generate a translation pair. Trying one more time.')
      retry_count += 1
  if len(translation_pairs) == 0:
    msg = f'{_subject_name} Could not generate any translation pairs in retry limit.'
    logger.critical(msg)
    raise ZeroTranslationPairsException(msg)
  return translation_pairs


# ~~~ entry point for LLM querying
def generate_translation_pairs(src_lang: str, tar_lang: str, template_dict: dict, **kwargs):
  ''''''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} ~~~ Starting to generate translation pairs')
  logger.debug(f'{_subject_name} src_lang = "{src_lang}"')
  logger.debug(f'{_subject_name} tar_lang = "{tar_lang}"')
  for k, v in template_dict.items():
    if '\n' in str(v): logger.debug(f'{_subject_name} {k} = "\n{v}\n"')
    else: logger.debug(f'{_subject_name} {k} = "{v}"')

  # 1 SIMPLIFY TEMPLATE
  simplification_dict = simplify_template(src_lang, template_dict, **kwargs)
  simplified_template = simplification_dict['simplified_template']
  simplified_template_origin = simplification_dict['simplified_template_origin']

  logger.info(f'{_subject_name} writing simplified templates to template_dict')
  template_dict['template'] = simplified_template
  template_dict['template_origin'] = simplified_template_origin

  logger.info(f'{_subject_name} simplified_template:\n{simplified_template}')
  logger.info(f'{_subject_name} simplified_template_origin:\n{simplified_template_origin}')
  p_utils.log_json_time(f'{_subject_name}_simplified-TEMPLATE-p_llm_gen.json', template_dict)

  # 2 GENERATE TWO PROGRAMS IN SRC LANG (TSP)
  tsp_dict = generate_tsp(src_lang, template_dict, **kwargs)
  n_tsps = tsp_dict['program_pairs']  # this is a list of tuples
  n_tnrdws = tsp_dict['templatized_nodes_replace_dot_w_star_flags']
  p_utils.log_json_time(f'{_subject_name}_gen-bestN-two-src-progs.json', n_tsps)
  p_utils.log_json_time(f'{_subject_name}_should-replace-dot-w-star.json', n_tnrdws)
  logger.debug(f'{_subject_name} Saving {len(n_tsps)} candidate TSPs.')
  assert len(n_tsps) == len(n_tnrdws)

  # ITERATE OVER BEST N TWO SOURCE PROGRAMS (SORTED BY PENALTY) AND TRANSLATE
  translation_pairs = None
  templatized_nodes_repdws = None
  tsp_counter = 0

  for (sp1, sp2), tnrdws in zip(n_tsps, n_tnrdws):
    tsp_counter += 1
    logger.debug(f'{_subject_name} (gen_trans_pair) Attempting to get translations of TSP {tsp_counter}/{len(n_tsps)}')
    logger.debug(f'{_subject_name} SP1:\n{sp1}')
    logger.debug(f'{_subject_name} SP2:\n{sp2}')

    templatized_nodes_repdws = tnrdws

    # 3 TRANSLATE SP1
    try:
      sp1_tp1_cands = translate_sp1(sp1, src_lang, tar_lang, template_dict, **kwargs)
      logger.info(f'{_subject_name} (gen_trans_pair) Generated {len(sp1_tp1_cands)} possible translations for SP1.')
    except SP1TranslationRetryLimitException:
      logger.info(f'{_subject_name} (gen_trans_pair) Reached retry limit when translating SP1. Will try with the next TSP if any.')
      continue

    # 4 TRANSLATE SP2
    try:
      translation_pairs = translate_sp2(sp2, src_lang, tar_lang, sp1_tp1_cands, template_dict, **kwargs)
    except ZeroTranslationPairsException:
      logger.info(f'{_subject_name} (gen_trans_pair) Could not generate a translation pair with TSP {tsp_counter}/{len(n_tsps)}. Will try with the next TSP if any.')
      continue

    break

  if translation_pairs is None:
    msg = f'{_subject_name} (gen_trans_pair) Could not generate a translation pair with any of {len(n_tsps)} TSPs. Please check the closest gen-bestN-two-src-progs.json file to check these TSPs.'
    msg += f'\ntemplate:\n{template_dict["template"]}\ntemplate_origin:\n{template_dict["template_origin"]}'
    logger.error(msg)
    raise ZeroTranslationPairsException(msg)

  return {
    'translation_pairs': translation_pairs,
    'templatized_nodes_replace_dws_values': templatized_nodes_repdws
  }


def _test_translate_sp1():
  test_harness_config:dict = p_utils.read_json('temporary_test_translate_sp1_config.json')
  best_N_tsp_fpath = Path(test_harness_config['best_n_tsp'])
  simpl_template_path = Path(test_harness_config['simpl_template'])

  best_N_tsps = p_utils.read_json(best_N_tsp_fpath)
  template_dict = p_utils.read_json(simpl_template_path)

  src_lang = template_dict['src_lang']
  tar_lang = template_dict['tar_lang']

  for (sp1, sp2) in best_N_tsps:
    sp1_tp1_cands = translate_sp1(sp1, src_lang, tar_lang, template_dict, subject_name='test-sp1')
    p_utils.write_json('temporary_test_translate_sp1.json', sp1_tp1_cands)

def _test_extract_code_blocks():
  ''''''
  test_harness_config:dict = p_utils.read_json('temporary_extract_code_blocks_config.json')
  llm_raw_response = p_utils.read_text(test_harness_config['llm_raw_response'])
  code_blocks = extract_code_blocks(llm_raw_response, subject_name='test-ext-cb')
  p_utils.write_json('temporary_extract_code_blocks.json', code_blocks)

def _test_get_best_n_tsps():
  test_harness_config:dict = p_utils.read_json('temporary_test_get_best_n_tsps_config.json')
  code_blocks_val_fpath = Path(test_harness_config['code_blocks_val_fpath'])
  best_n = test_harness_config['best_n']

  code_blocks_val_dict = p_utils.read_json(code_blocks_val_fpath)

  result = _get_best_n_tsps(code_blocks_val_dict['valid_tsp_lists_sorted'], best_n)
  p_utils.write_json('temporary_test_get_best_n_tsps.json', result)

if __name__ == '__main__':
  # _test_translate_sp1()
  # _test_extract_code_blocks()
  _test_get_best_n_tsps()
