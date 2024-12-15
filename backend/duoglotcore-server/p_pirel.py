from typing import Callable, Any, Tuple
import timeit
import traceback
import json
import logging
from tree_sitter import Language
from pathlib import Path

import p_translators
import p_consts
import p_llm_gen
import p_utils
import grammar_expand
import ast_pretty
import ast_parse


logger = logging.getLogger(__name__)


def _get_hacky_rule(problematic_node_type: str, secret_identifier: str) -> str:
  ''''''
  matcher = f'"py.{problematic_node_type}" "*"'
  expander = f'"js.identifier" (val "{secret_identifier}")'
  hacky_rule = f'(match_expand (fragment ({matcher}) "*") (fragment ({expander}) "*2"))'
  return hacky_rule

def _get_hacky_rule_2(problematic_node_type: str, secret_identifier: str) -> str:
  ''''''
  matcher = f'"py.{problematic_node_type}" "*"'
  expander = f'"js.expression_statement" ("js.identifier" (val "{secret_identifier}"))'
  hacky_rule = f'(match_expand (fragment ({matcher}) "*") (fragment ({expander}) "*2"))'
  return hacky_rule


def _get_partial_program(
  templates_dict: dict,
  template_dict: dict,
  trans_rules: str,
  src_lang: str,
  tar_lang: str,
  target_grammar: dict,
  _optional_dbg_info_save_func: Callable,
  slot_dedup_enabled: bool,
  choices: dict,
  auto_backward: bool,
  **kwargs,
) -> str:

  def __post_process_partial_program_remove_excess_replace_vars(partial_program: str) -> str:
    '''
    Problem: if a problematic node appears multiple times consecutively in the AST,
    what ends up happening is that partial program contains several consecutive
    replace_var's. This is not good for using with LLMs.
    This function solves this problem by str.replace() by replacing all occurences of
    replace_var's to dummy_var's except the first one.
    The solution is somewhat hacky and not complete, but it's much easier than
    intervening translation process where we require translate() to use different
    rules for the same consecutive node types.
    '''
    li = partial_program.rsplit(
      p_consts.PAR_PROG_PROB_NODE_REPLACE,
      partial_program.count(p_consts.PAR_PROG_PROB_NODE_REPLACE) - 1
    )
    return p_consts.PAR_PROG_DUMMY_IDENTIFIER.join(li)

  _subject_name = kwargs['subject_name']

  # NOTE if the first translation was successful, it means we have all necessary translation rules.
  # If it wasn't successful, then we run a loop in which we introduce `problematic_node -> identifier` rules
  # until we translate the program. This way we generate a partial program.
  logger.warning(f'{_subject_name} First translation was not successful. Entering a partial program generation loop.')

  # 1 ADD HACKY RULES FOR THE MAIN PROBLEMATIC NODE
  prob_ntype_main = templates_dict['problematic_node_type']
  hr1 = _get_hacky_rule(prob_ntype_main, p_consts.PAR_PROG_PROB_NODE_REPLACE)
  hr2 = _get_hacky_rule_2(prob_ntype_main, p_consts.PAR_PROG_PROB_NODE_REPLACE)
  new_trans_rules = trans_rules + f'\n\n{hr1}\n\n{hr2}'

  new_src_code = template_dict['template_origin']
  new_src_ast, new_src_ann = ast_parse.parse_text_dbg(new_src_code, 'py')

  logger.info(f'{_subject_name} problematic_node_type_main = "{prob_ntype_main}"')
  logger.info(f'{_subject_name} Appended hacky rules for the main problematic node to the ruleset')
  logger.info(f'{_subject_name} new_src_code = \n{new_src_code}')

  new_translator = p_translators.get_translator(
    new_src_code, new_src_ast, new_src_ann, src_lang, tar_lang, target_grammar,
    new_trans_rules, _optional_dbg_info_save_func, slot_dedup_enabled)
  is_successful, tar_ast, choices_dict, error_info, dbg_history = new_translator.get_translation(choices, auto_backward, **kwargs)
  if is_successful:
    logger.info(f'{_subject_name} Success. Partial program generation is complete. num_loops=1')
    code, map_to_exid = ast_pretty.ast_to_code(tar_ast, tar_lang)
    return code

  # 2 ADD HACKY RULES FOR SUBSEQUENT PROBLEMATIC NODES
  logger.info(f'{_subject_name} Translation is not over yet: there are still nodes to translate')
  loop_counter = 1
  while not is_successful:
    logger.info(f'{_subject_name} Entering partial program generation loop-{loop_counter}')

    # TODO in case of NormalException, error_info may not contain templates_dict
    templates_dict = json.loads(error_info['templates_dict'])
    prob_ntype_remaining = templates_dict['problematic_node_type']
    hr1 = _get_hacky_rule(prob_ntype_remaining, p_consts.PAR_PROG_DUMMY_IDENTIFIER)
    hr2 = _get_hacky_rule_2(prob_ntype_remaining, p_consts.PAR_PROG_DUMMY_IDENTIFIER)
    new_trans_rules = new_trans_rules + f'\n\n{hr1}\n\n{hr2}'

    logger.info(f'{_subject_name} prob_ntype_remaining = "{prob_ntype_remaining}"')
    logger.info(f'{_subject_name} Appended hacky rules to the ruleset')

    new_translator = p_translators.get_translator(
      new_src_code, new_src_ast, new_src_ann, src_lang, tar_lang, target_grammar,
      new_trans_rules, _optional_dbg_info_save_func, slot_dedup_enabled)
    is_successful, tar_ast, choices_dict, error_info, dbg_history = new_translator.get_translation(choices, auto_backward, **kwargs)

    logger.info(f'{_subject_name} Partial program generation loop-{loop_counter} ended: is_successful={is_successful}')
    loop_counter += 1

  logger.info(f'{_subject_name} Success. Partial program generation is complete. num_loops={loop_counter}')
  code, map_to_exid = ast_pretty.ast_to_code(tar_ast, tar_lang)

  # NOTE refer to the docs on why we are doing this
  partial_program = __post_process_partial_program_remove_excess_replace_vars(code)

  return partial_program


def _translation_failed_run_pirel(
  trans_rules: str,
  error_info: dict,
  src_lang: str,
  tar_lang: str,
  target_grammar: dict,
  _optional_dbg_info_save_func: Callable,
  slot_dedup_enabled: bool,
  choices: dict,
  auto_backward: bool,
  translator_dbg_info,
  **kwargs
) -> dict:
  ''''''
  _subject_name = kwargs['subject_name']

  templates_dict = json.loads(error_info['templates_dict'])
  template_dict = templates_dict[str(templates_dict['num_templates'] - 1)]
  template_dict['src_lang'] = templates_dict['src_lang']
  template_dict['tar_lang'] = templates_dict['tar_lang']

  partial_program = _get_partial_program(
    templates_dict,
    template_dict,
    trans_rules,
    src_lang,
    tar_lang,
    target_grammar,
    _optional_dbg_info_save_func,
    slot_dedup_enabled,
    choices,
    auto_backward,
    **kwargs
  )

  logger.info(f'{_subject_name} Here is the generated partial program:\n{partial_program}')
  template_dict['partial_program'] = partial_program
  p_utils.log_json_time(f'{_subject_name}_TEMPLATE_p_pirel.json', template_dict)

  # GENERATE TRANSLATION PAIRS
  # TODO handle errors of generate_translation_pairs()
  translation_pairs = p_llm_gen.generate_translation_pairs(src_lang, tar_lang, template_dict, **kwargs)
  p_utils.log_json_time(f'{_subject_name}_translation-pairs.json', translation_pairs)
  logger.info(f'{_subject_name} Translation pair generation is complete')

  return {
    'pirel': {
      'translation_pairs': translation_pairs,
      'template_dict': template_dict
    }
  }


def _init_translation(
  src_code: str,
  src_lang: str,
  tar_lang: str,
  trans_rules: str,
  choices: dict,
  _optional_dbg_info_save_func: Callable
) -> Tuple[grammar_expand.TransSession, list, dict, dict, bool, dict]:
  '''
  no choices means default choices
  '''
  # sanity check
  if not src_code.isascii():
    return {"error_info":{"type": "API_PARAM_ERROR", "msg": "src_code is not ascii."}}
  assert choices["type"] in ["STEP", "ASTNODE"], "Unknown choices type"

  # useful local vars
  slot_dedup_enabled = choices["type"] == "ASTNODE"
  target_grammar = p_consts.GRAMMAR_DICT[tar_lang]
  src_ast, src_ann = ast_parse.parse_text_dbg(src_code, src_lang)

  # translator
  translator = p_translators.get_translator(
    src_code,
    src_ast,
    src_ann,
    src_lang,
    tar_lang,
    target_grammar,
    trans_rules,
    _optional_dbg_info_save_func,
    slot_dedup_enabled
  )
  translator_dbg_info = translator.get_session_dbg_info()

  return translator, src_ast, src_ann, target_grammar, slot_dedup_enabled, translator_dbg_info


def translate(
  src_code: str,
  src_lang: str,
  tar_lang: str,
  trans_rules: str,
  auto_backward: bool,
  choices: dict,
  _optional_dbg_info_save_func: Callable,
  **kwargs
) -> dict:
  '''
  Entry point for PiREL translation
  '''

  subject_name = kwargs['subject_name']
  pirel_enabled = kwargs['pirel_enabled']
  logger.info(f'\n\n\n\n{subject_name} p_pirel.translate(): Starting PiREL')

  translator, src_ast, src_ann, target_grammar, slot_dedup_enabled, translator_dbg_info = _init_translation(
    src_code,
    src_lang,
    tar_lang,
    trans_rules,
    choices,
    _optional_dbg_info_save_func
  )

  trans_st = timeit.default_timer()
  is_successful, tar_ast, choices_dict, error_info, dbg_history = translator.get_translation(choices, auto_backward, **kwargs)
  trans_et = timeit.default_timer()

  # TRANSLATION IS SUCCESSFUL
  if is_successful:
    logger.info(f'{subject_name} SUCCESS. Translation is successful!')
    pretty_st = timeit.default_timer()
    code, map_to_exid = ast_pretty.ast_to_code(tar_ast, tar_lang)
    pretty_et = timeit.default_timer()

    return {
      "parse": {"src_ast": src_ast, "src_ann": src_ann},
      "timespan": trans_et - trans_st,
      "timespan_p": pretty_et - pretty_st,
      "result": {"ast": tar_ast, "code": code, "map_to_exid": map_to_exid},
      "dbg_history": dbg_history,
      "translator_dbg_info": translator_dbg_info
    }

  # TRANSLATION IS NOT SUCCESSFUL, PIREL IS NOT ENABLED
  if not pirel_enabled:
    logger.error(f'{subject_name} Translation is not successful! PiREL is not enabled!')
    return {
      "parse": {"src_ast": src_ast, "src_ann": src_ann},
      "timespan": trans_et - trans_st,
      "timespan_p": None,
      "error_info": error_info,
      "dbg_history": dbg_history,
      "translator_dbg_info": translator_dbg_info
    }

  # TRANSLATION IS NOT SUCCESSFUL, PIREL IS ENABLED
  logger.warning(f'{subject_name} Translation is not successful! PiREL is enabled!')
  if not 'templates_dict' in error_info:
    msg = f'{subject_name} Cannot continue further due to an error on the backend:\n{error_info["msg"]}'
    logger.critical(msg)
    raise RuntimeError(msg)

  return _translation_failed_run_pirel(
    trans_rules,
    error_info,
    src_lang,
    tar_lang,
    target_grammar,
    _optional_dbg_info_save_func,
    slot_dedup_enabled,
    choices,
    auto_backward,
    translator_dbg_info,
    **kwargs
  )


def test_translate():
  '''
  src_code
  src_lang
  tar_lang
  trans_rules
  auto_backward
  choices
  _optional_dbg_info_save_func
  pirel_enabled
  '''
  src_code_fpath = Path('/code/repo-duoglot/backend/duoglotcore-server/pirel-logs/debug-11-multiple-var-to-replace/02-26-14-31-04.752348-program_to_translate.py')
  src_code = p_utils.read_text(src_code_fpath)
  src_lang = 'py'
  tar_lang = 'js'
  trans_rules_fpath = Path('/code/repo-duoglot/data/duoglot/tests/trans_programs/py_js/base_fn_header_only_ext.snart')
  trans_rules = p_utils.read_text(trans_rules_fpath)
  auto_backward = True
  choices = {'type': 'STEP', 'choices_list': []}
  _optional_dbg_info_save_func = print
  pirel_enabled = True

  result_dict = translate(
    src_code,
    src_lang,
    tar_lang,
    trans_rules,
    auto_backward,
    choices,
    _optional_dbg_info_save_func,
    pirel_enabled
  )

  p_utils.write_json('temporary_test_translate.json', result_dict)

if __name__ == '__main__':
  test_translate()
