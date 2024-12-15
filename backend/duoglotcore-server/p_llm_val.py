import math
import logging
from typing import List, Tuple, Union, Dict
from pathlib import Path

import p_consts
import p_utils
import p_data_structures as pds
import ast_parse

logger = logging.getLogger(__name__)


def val_simplified_template_candidates(
  src_lang: str,
  template_origin: str,
  templatized_node_ids_context: dict,
  simplified_template_candidates: List[str],
  **kwargs
):
  '''
  Simplified templates should satisfy the following criteria:
  1. Should be parseable
  2. Everything except templatized nodes should be identical to template origin
  3. Simplest AST at templatized nodes.
  How do we measure simplicity? Should not exceed depth N.
  '''
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Starting validation of {len(simplified_template_candidates)} "Simplified Template" candidates')

  return_dict = {}
  return_dict['simplified_template_candidates_stats'] = []

  # 1 get the stats for simplified templates
  for i, simplified_template_cand in enumerate(simplified_template_candidates):
    result_dict = _analyze_simplified_template_candidate(
      simplified_template_cand,
      template_origin,
      templatized_node_ids_context,
      src_lang
    )
    return_dict['simplified_template_candidates_stats'].append([i, result_dict])

  # 2 filter programs that satisfy our criteria
  return_dict['simplified_template'] = None
  return_dict['templatized_node_texts'] = None
  max_overall_depth = 1e10
  for i, st_cand_stats in return_dict['simplified_template_candidates_stats']:
    if st_cand_stats['has_parse_error']:
      continue
    if not st_cand_stats['is_type_isomorphic_to_template_origin']:
      continue
    depths = st_cand_stats['depths_at_templatized_nodes']
    if not all(map(lambda depth: depth <= p_consts.LLM_VAL_TS_MAX_DEPTH, depths)):
      continue
    if sum(depths) < max_overall_depth:
      return_dict['simplified_template'] = st_cand_stats['simplified_template_candidate']
      return_dict['templatized_node_texts'] = st_cand_stats['texts_at_templatized_nodes']
      max_overall_depth = sum(depths)

  return return_dict

def _analyze_simplified_template_candidate(
  simplified_template_cand: str,
  template_origin: str,
  templatized_node_ids_context: dict,
  src_lang: str
) -> dict:
  ''''''
  return_dict = {}
  return_dict["template_origin"] = template_origin
  return_dict["simplified_template_candidate"] = simplified_template_cand
  return_dict["has_parse_error"] = None
  return_dict["is_type_isomorphic_to_template_origin"] = None
  return_dict["depths_at_templatized_nodes"] = []
  return_dict["texts_at_templatized_nodes"] = []

  # check for criteria #1 - parse error
  return_dict["has_parse_error"] = p_utils.does_have_parse_error(simplified_template_cand, src_lang)

  if return_dict["has_parse_error"]:
    return return_dict

  # check for criteria #2 - type isomorphism with template
  templatized_node_paths = list(templatized_node_ids_context.values())
  simplified_template_ast_text, _ = ast_parse.parse_text_dbg(simplified_template_cand, src_lang, keep_text=True)
  template_origin_ast_text, _ = ast_parse.parse_text_dbg(template_origin, src_lang, keep_text=True)

  simplified_template_tree = pds.PirelTree(simplified_template_ast_text)
  template_origin_tree = pds.PirelTree(template_origin_ast_text)

  return_dict["is_type_isomorphic_to_template_origin"] = _is_generated_code_type_isomorphic_to_shallow_template(
    simplified_template_tree,
    template_origin_tree,
    templatized_node_paths
  )

  if not return_dict["is_type_isomorphic_to_template_origin"]:
    return return_dict

  # check for criteria #3 - collect depths of templatized nodes
  simplified_template_tree._fix_indentation()
  root_node = simplified_template_tree.get_root_node()

  if len(root_node.get_children()) != 1:
    return return_dict

  for templatized_node_path in templatized_node_paths:
    context_node = root_node.get_children()[0]
    templatized_node = context_node.get_child_by_path(templatized_node_path)
    tn_depth = templatized_node.get_depth()
    tn_text = templatized_node.get_text()
    return_dict["depths_at_templatized_nodes"].append(tn_depth)
    return_dict["texts_at_templatized_nodes"].append(tn_text)

  return return_dict


def val_tsp_candidates(
  src_lang: str,
  template_origin: str,
  templatized_node_ids: Dict[str, List[int]],
  generated_code_blocks: List[str],
  is_insert_secret_fn: bool,
  **kwargs
):
  '''
  TODO do we still need `is_insert_secret_fn`?

  PARAMS:
  templatized_node_ids = {'node_id': node_path}

  Generated Code Blocks -> THIS FUNCTION -> Two Source Programs

  Generating TSPs is a two-step process.

  ~~~ In the first step,
  we filter generated code blocks to keep only valid ones.
  The generated code blocks must satisfy the following hard conditions:

  1. Have no parse errors
  2. Are identical to template except at templatized nodes (a.k.a is_type_isomorphic_to_template)

  ~~~ In the second step,
  we form pairs from the remaining code blocks and check if they satisfy
  the following hard criteria:

  3. Unification of TSPs match template origin (i.e. a matcher, obtained from unification of TSPs,
  can match the template origin). This is a hard condition and must be satisfied.
  4. Templatized nodes have no repeating terminal tokens

  and the following soft criteria, that define the ranking of TSP candidates:
  5.

  Notes:
  1. Criteria #1 and criteria #2 are hard and must be satisfied
  2. Criteria #3 and criteria #4 are hard and must be satisfied


  # NOTE old below
  3. at templatized nodes ((a xor b) and c and d): TODO update this section
    a. string of NT-NT-T nodes of width 1 (includes max_depth=2) (guarantees single T token)
    b. different node types (doesn't guarantee single T token)
    c. no repeating terminal tokens (may conflict with {b})
    d. abstraction of code blocks matches template origin

  Notes on {3}:
  (i) It is preferred to have {a} over {b}, because we are guaranteed to have a single T token.
  However, it is not always possible as in the case of typed_parameter `nums: List[int]`.
  `__: __` would give programs such as `a: int`, `b: float` (ident: type.ident).
  Rule learned from that pair doesn't translate `nums: List[int]` (ident: type.subscript.ident-ident)
  (ii) {d} guarantees that the two source programs, when unified, match the template origin,
  thus allowing to infer a valid rule (may overfit in the worst case).
  (iii) Include a metric that allows ranking two source programs regarding {a} and {b}.

  We assume that the template is filled with literals and identifiers
  '''
  num_code_blocks_raw = len(generated_code_blocks)
  _subject_name = kwargs['subject_name']
  logger.info(f'{_subject_name} Starting validation of {num_code_blocks_raw} unverified "Two Source Programs" candidates')

  assert len(templatized_node_ids) > 0, 'there should be AT LEAST ONE templatized node'

  def __get_tsp_min_penalty(filtered_program_pairs: List[dict], config: str) -> dict:
    '''min penalty is the best'''
    assert len(filtered_program_pairs) > 0
    min_penalty = filtered_program_pairs[0]['pair_penalties'][config]
    best_pp = filtered_program_pairs[0]
    for fpp in filtered_program_pairs[1:]:
      if fpp['pair_penalties'][config] < min_penalty:
        min_penalty = fpp['pair_penalties'][config]
        best_pp = fpp
    return best_pp

  def __sorted_filtered_tsp_by_penalty(filtered_program_pairs: List[dict], config: str) -> List[dict]:
    '''min penalty is the best'''
    assert len(filtered_program_pairs) > 0
    sorted_program_pairs = sorted(filtered_program_pairs, key=lambda tsps: tsps['pair_penalties'][config])
    return sorted_program_pairs

  return_dict = {
    'template_origin': template_origin,
    'num_code_blocks_raw': num_code_blocks_raw,
    'num_code_blocks_filtered': None,
    'generated_code_blocks_stats': [],
    'filtered_code_blocks_stats': [],
    'num_candidate_tsps': None,
    'num_candidate_tsps_filtered': None,
    'tsp_stats': [],
    'success': None,
    'min_penalties': {},
    'valid_tsp_lists_sorted': {},
  }

  template_origin_tree = pds.DuoGlotTree.from_code_str(template_origin, src_lang)

  # ~~~ 1 collect the data for criteria #1 and criteria #2
  logger.debug(f'{_subject_name} Checking {num_code_blocks_raw} generated code blocks to see if they have parse errors and are type-isomorphic to template')
  for i, generated_code_block in enumerate(generated_code_blocks):
    result_dict = _gen_code_block_filter_crit_1_2(
      generated_code_block,
      template_origin_tree,
      templatized_node_ids,
      src_lang,
      **kwargs
    )
    return_dict['generated_code_blocks_stats'].append([i, result_dict])

  # 2 keep code blocks that satisfy criteria #1 and criteria #2
  # keep code blocks with unique encodings
  filtered_code_blocks_stats = []
  encodings_set = []
  for i, gen_code_stats in return_dict['generated_code_blocks_stats']:
    # criteria #1 and criteria #2
    if not gen_code_stats['passes_hard_criteria']:
      continue
    # allow up to 2 code blocks with the same encoding
    # this ensures that there is a chance of _val_ placeholder match
    if encodings_set.count(gen_code_stats['encoding']) < 2:
      filtered_code_blocks_stats.append(gen_code_stats)
      encodings_set.append(gen_code_stats['encoding'])
  return_dict['filtered_code_blocks_stats'] = filtered_code_blocks_stats

  num_code_blocks_filtered = len(filtered_code_blocks_stats)
  num_candidate_tsps = num_code_blocks_filtered * (num_code_blocks_filtered - 1) // 2
  return_dict['num_code_blocks_filtered'] = num_code_blocks_filtered
  return_dict['num_candidate_tsps'] = num_candidate_tsps

  logger.debug(f'{_subject_name} {num_code_blocks_filtered}/{num_code_blocks_raw} programs are usable after filtering step')

  # not enough programs for pairs
  if num_code_blocks_filtered < 2:
    logger.info(f'{_subject_name} Not enough filtered programs: {num_code_blocks_filtered}')
    return_dict['success'] = False
    return return_dict

  # ~~~ 3 iterate over all possible pairs and collect analysis
  logger.info(f'{_subject_name} Collecting analysis results for all {num_candidate_tsps} "Two Source Programs" candidates')
  for i in range(num_code_blocks_filtered - 1):
    for j in range(i + 1, num_code_blocks_filtered):
      sp1_tree = filtered_code_blocks_stats[i]['generated_code_block_duoglot_tree']
      sp2_tree = filtered_code_blocks_stats[j]['generated_code_block_duoglot_tree']
      tsp_analysis_results = _tsp_candidate_analyze(
        sp1_tree, sp2_tree,
        template_origin_tree, templatized_node_ids,
        is_insert_secret_fn,
        penalty_coefs_dict=p_consts.PENALTY_COEFS_DICT
      )
      sp1 = filtered_code_blocks_stats[i]['generated_code_block']
      sp2 = filtered_code_blocks_stats[j]['generated_code_block']
      sp1_encoding = filtered_code_blocks_stats[i]['encoding']
      sp2_encoding = filtered_code_blocks_stats[j]['encoding']
      tsp_analysis_results['sp1'] = sp1
      tsp_analysis_results['sp2'] = sp2
      tsp_analysis_results['sp1_encoding'] = sp1_encoding
      tsp_analysis_results['sp2_encoding'] = sp2_encoding
      return_dict['tsp_stats'].append(tsp_analysis_results)

  # 4 keep TSP candidates that satisfy criteria #3 and criteria #4
  filtered_tsp_stats = []
  for tsp_stat in return_dict['tsp_stats']:
    if tsp_stat['passes_hard_criteria']:
      filtered_tsp_stats.append(tsp_stat)

  return_dict['num_candidate_tsps_filtered'] = len(filtered_tsp_stats)

  # this signals to query LLM again
  if len(filtered_tsp_stats) == 0:
    logger.info(f'{_subject_name} Not enough TSP candidates: 0')
    return_dict['success'] = False
    return return_dict

  return_dict['success'] = True

  for config in p_consts.PENALTY_COEFS_DICT.keys():
    # best available program pair
    best_available_tsp = __get_tsp_min_penalty(filtered_tsp_stats, config)
    return_dict['min_penalties'][config] = best_available_tsp['pair_penalties'][config]

    # all valid program pairs sorted by score (if the best doesn't work)
    # NOTE we need this, because the best program pair may not be easy to translate to target language
    return_dict['valid_tsp_lists_sorted'][config] = __sorted_filtered_tsp_by_penalty(filtered_tsp_stats, config)

  return return_dict

def _gen_code_block_filter_crit_1_2(
  generated_code_block: str,
  template_origin_tree: pds.DuoGlotTree,
  templatized_node_ids: dict,
  src_lang: str,
  **kwargs
) -> dict:
  '''
  Given a single generated code block and its template origin,
  check if the generated code block satisfies the following criteria:
  1. Generated code block has no parse errors
  2. Generated code block is identical to template except at templatized nodes (a.k.a is_type_isomorphic_to_template)

  TERMS:
  generated_code_block - a single program generated by LLM by filling holes in a template.
  template_origin - a piece of code from which the template was generated.
  templatized_node_ids - path to templatized nodes and their ids
  src_lang - a short representation of a programming language (e.g. py, js, etc)
  MAX_DEPTH - max depth for nodes at templatized nodes

  RETURN FORMAT
  returnData = {
    generated_code_block: str
    template_origin: str,
    has_parse_error: bool,
    is_type_isomorphic_to_template: bool,
  }
  '''
  return_data = {
    'generated_code_block': generated_code_block,
    'has_parse_error': None,
    'generated_code_block_duoglot_tree': None,
    'encoding': None,
    'is_type_isomorphic_to_template': None,
    'passes_hard_criteria': None
  }

  # check for criteria #1 - parse error
  try:
    generated_code_tree = pds.DuoGlotTree.from_code_str(generated_code_block, src_lang)
    return_data['has_parse_error'] = False
    return_data['generated_code_block_duoglot_tree'] = generated_code_tree
    return_data['encoding'] = _get_type_ahu_encoding_x_ident(generated_code_tree)
  except pds.TreeConstructionError:
    return_data['has_parse_error'] = True
    return_data['passes_hard_criteria'] = False
    return return_data
  # NOTE this piece of code may throw away syntactically correct pieces of code (not verified)
  # it can be removed after strengthening the regular expression that parses raw response from LLM
  # refer to p_llm_gen.extract_code_blocks()
  # this is probably an error from ast_parse.parse_text_dbg()
  except AssertionError as err:
    _subject_name = kwargs['subject_name']
    logger.warning(
      f'{_subject_name} p_llm_val._gen_code_block_filter_crit_1_2(): throwing away the following code block:\n'
      f'"\n{generated_code_block}\n"\n'
      f'due to AssertionError (probably from ast_parse.parse_text_dbg):\n"{err}"'
    )
    return_data['has_parse_error'] = True
    return_data['passes_hard_criteria'] = False
    return return_data

  # check for criteria #2 - type isomorphism with template
  templatized_node_paths = list(templatized_node_ids.values())
  is_type_isomorphic_to_template = _is_generated_code_type_isomorphic_to_shallow_template(
    generated_code_tree,
    template_origin_tree,
    templatized_node_paths
  )
  return_data['is_type_isomorphic_to_template'] = is_type_isomorphic_to_template
  return_data['passes_hard_criteria'] = is_type_isomorphic_to_template
  return return_data

def _tsp_candidate_analyze(
  sp1_tree: pds.DuoGlotTree,
  sp2_tree: pds.DuoGlotTree,
  template_origin_tree: pds.DuoGlotTree,
  templatized_node_ids: dict,
  is_insert_secret_fn: bool,
  penalty_coefs_dict: Dict[str, Dict[str, float]]
) -> dict:
  '''
  INTERNAL
  pair_penalty - a value that is used for ranking pairs of programs
  in source language. The smaller the value, the better the pair.

  Configure penalty calculation with penalty_coefs.
  Refer to its structure in p_consts.PENALTY_COEFS_DEFAULT

  NOTES
  1. All templatized nodes at sp1 and sp2, when unified,
  should match a templatized node at template origin.

  RETURN
  do all nodes match when unified? score for the pair
  '''

  def __mean_num_tokens(num1: int, num2: int) -> float:
    '''
    smaller is better
    favor closer values over distant ones
    '''
    return math.sqrt(num1 * num1 + num2 * num2) / math.sqrt(2)

  return_dict = {
    'tree1': sp1_tree,
    'tree2': sp2_tree,
    'tns_can_match_values': None,
    'tns_max_match_depth_values': None,
    'templatized_nodes_replace_dot_w_star_flags': None,
    'tns_match_types': None,
    'sp1_T_id_lit_tokens': None,
    'sp2_T_id_lit_tokens': None,
    'sp1_T_tokens': None,
    'sp2_T_tokens': None,
    'tns_penalties': None,
    'match_penalties': None,
    'pair_penalties': None,
    'all_templatized_nodes_match': None,
    'no_repeating_tokens': None,
    'passes_hard_criteria': None,
  }

  # artifacts to collect
  tns_can_match_values = []
  tns_max_match_depth_values = []
  tns_should_replace_values = []
  tns_match_types = []
  sp1_T_id_lit_tokens = {}
  sp2_T_id_lit_tokens = {}
  sp1_T_tokens = {}
  sp2_T_tokens = {}

  tns_penalties = {}
  match_penalties = {}
  pair_penalties = {}

  # iterate over templatized nodes
  for node_id, tn_path in templatized_node_ids.items():

    # 1 get templatized nodes at node_id
    sp1_tn = _get_templatized_node(sp1_tree, tn_path)
    sp2_tn = _get_templatized_node(sp2_tree, tn_path)
    tor_tn = _get_templatized_node(template_origin_tree, tn_path)

    # NOTE should_replace does not consider multiple ph nodes under a template node
    unif_res_dict = _unification_of_template_nodes_can_match(sp1_tn, sp2_tn, tor_tn, is_insert_secret_fn)
    can_match : bool = unif_res_dict['unification_matches']
    max_match_depth : int = unif_res_dict['max_match_depth']
    should_replace : Union[bool, list] = unif_res_dict['replace_dot_with_star']
    match_types : Union[str, list] = unif_res_dict['match_type']

    # this condition covers cases where problematic node already has a single terminal child
    # such as literal nodes (int, float, bool, etc.) or identifier nodes.
    # this case also appears in p_templates.TemplateTree.node_can_be_templatized_template_node()
    if tor_tn.has_single_terminal_child():
      assert isinstance(match_types, str)
      # NOTE the two independent if-statements below may be combined (in what case?)
      # all node types must be identical
      if not (sp1_tn.get_type() == sp2_tn.get_type() == tor_tn.get_type()):
        can_match = False
      # unification type must be p_consts.MATCH_TYPE_TV
      if match_types != p_consts.MATCH_TYPE_TV:
        can_match = False

    tns_can_match_values.append(can_match)
    tns_max_match_depth_values.append(max_match_depth)
    tns_should_replace_values.append(should_replace)
    tns_match_types.append(match_types)

    # tokens
    sp1_node_T_id_lit_tokens = sp1_tn.get_terminal_tokens(is_skip_grammar_terminal=True)
    sp2_node_T_id_lit_tokens = sp2_tn.get_terminal_tokens(is_skip_grammar_terminal=True)
    sp1_T_id_lit_tokens[int(node_id)] = sp1_node_T_id_lit_tokens
    sp2_T_id_lit_tokens[int(node_id)] = sp2_node_T_id_lit_tokens

    sp1_node_T_tokens = sp1_tn.get_terminal_tokens(is_skip_grammar_terminal=False)
    sp2_node_T_tokens = sp2_tn.get_terminal_tokens(is_skip_grammar_terminal=False)
    sp1_T_tokens[int(node_id)] = sp1_node_T_tokens
    sp2_T_tokens[int(node_id)] = sp2_node_T_tokens

    # calculate mean number of tokens based on ALL terminal tokens
    mean_num_tokens = __mean_num_tokens(len(sp1_node_T_tokens), len(sp2_node_T_tokens))

    # templatized node contains only grammar terminals
    cnt_grammar_terminals_only = 0
    cnt_grammar_terminals_only += int(len(sp1_node_T_id_lit_tokens) == 0 and len(sp1_node_T_tokens) > 0)
    cnt_grammar_terminals_only += int(len(sp2_node_T_id_lit_tokens) == 0 and len(sp2_node_T_tokens) > 0)

    # check for string of NT-NT-T nodes of width 1
    ast_width1 = int(sp1_tn.is_ast_width_1()) + int(sp2_tn.is_ast_width_1())

    # should_replace: penalize "." to "*" conversions
    # the idea is to keep dots as much as possible

    for pen_cfg, penalty_coefs in penalty_coefs_dict.items():
      tn_penalty = \
        penalty_coefs['max_match_depth'] * max_match_depth + \
        penalty_coefs['mean_num_tokens'] * mean_num_tokens + \
        penalty_coefs['should_replace'] * _calculate_should_replace_penalty(should_replace) + \
        penalty_coefs['ast_width1'] * ast_width1 + \
        penalty_coefs['grammar_terminals_only'] * cnt_grammar_terminals_only + \
        penalty_coefs['tn_bias']
      # less is better
      tns_penalties.setdefault(pen_cfg, []).append(tn_penalty)

  for pen_cfg, penalty_coefs in penalty_coefs_dict.items():

    # match penalty
    match_penalty = _calculate_match_penalty(tns_match_types, penalty_coefs['match_penalty_coefs'])
    match_penalties[pen_cfg] = match_penalty

    # sum of squares
    pair_penalty = \
      penalty_coefs['tns_penalties'] * sum(tns_penalties[pen_cfg]) + \
      penalty_coefs['match_penalty'] * match_penalty + \
      penalty_coefs['pair_bias']
    pair_penalties[pen_cfg] = pair_penalty

  # hard constraint #1
  all_templatized_nodes_match = all(tns_can_match_values)

  # hard constraint #2
  # evaluate no_repeating_tokens based on identifier, literal terminal tokens ONLY
  # NOTE no repeating tokens can be false iff the holes are filled with single tokens
  # forcing this condition otherwise on complex hole fills is too restrictive
  no_repeating_tokens = not _has_repeating_tokens(sp1_T_id_lit_tokens, sp2_T_id_lit_tokens)

  return_dict['tns_can_match_values'] = tns_can_match_values
  return_dict['tns_max_match_depth_values'] = tns_max_match_depth_values
  return_dict['templatized_nodes_replace_dot_w_star_flags'] = tns_should_replace_values
  return_dict['tns_match_types'] = tns_match_types
  return_dict['sp1_T_id_lit_tokens'] = sp1_T_id_lit_tokens
  return_dict['sp2_T_id_lit_tokens'] = sp2_T_id_lit_tokens
  return_dict['sp1_T_tokens'] = sp1_T_tokens
  return_dict['sp2_T_tokens'] = sp2_T_tokens
  return_dict['tns_penalties'] = tns_penalties
  return_dict['match_penalties'] = match_penalties
  return_dict['pair_penalties'] = pair_penalties
  return_dict['all_templatized_nodes_match'] = all_templatized_nodes_match
  return_dict['no_repeating_tokens'] = no_repeating_tokens
  return_dict['passes_hard_criteria'] = all_templatized_nodes_match and no_repeating_tokens

  return return_dict

def _get_templatized_node(tree: pds.DuoGlotTree, path: List[int]) -> pds.DuoGlotNode:
  ''''''
  root_node = tree.get_root_node()
  assert len(root_node.get_children()) == 1, 'should not happen'
  context_node = root_node.get_children()[0]
  templatized_node = context_node.get_child_by_path(path)
  return templatized_node

def _unification_of_template_nodes_can_match(
  sp1_tn: pds.DuoGlotNode,
  sp2_tn: pds.DuoGlotNode,
  tor_tn: pds.DuoGlotNode,
  is_insert_secret_fn: bool
) -> dict:
  '''
  RETURN
  Dictionary: {
    unification_matches: bool,
    max_match_depth: int,
    replace_dot_with_star: bool,
    match_type: str
  }

  sp1_tn, sp2_tn, tor_tn - corresponding templatized nodes at
  SP1, SP2, and template origin
  '''
  def __rec_does_unification_match(
    sp1_tn: pds.DuoGlotNode,
    sp2_tn: pds.DuoGlotNode,
    tor_tn: pds.DuoGlotNode,
    current_depth: int
  ) -> dict:
    '''
    Does the unification of sp1_tn and sp2_tn match tor_tn?

    RETURN
    Dictionary: {
      unification_matches: bool,
      max_match_depth: int,
      replace_dot_with_star: bool,
      match_type: str
    }
    '''
    return_dict = {
      'unification_matches': None,
      'max_match_depth': None,
      'replace_dot_with_star': None,
      'match_type': None
    }

    # T-NT-?
    if sp1_tn.is_terminal() and sp2_tn.is_nonterminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    # NT-T-?
    if sp1_tn.is_nonterminal() and sp2_tn.is_terminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    # T-T-?
    if sp1_tn.is_terminal() and sp2_tn.is_terminal():

      # T-T-NT
      if tor_tn.is_nonterminal():
        return_dict['unification_matches'] = False
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = False
        return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
        return return_dict

      # T-T-T (scope invariant)

      if sp1_tn.get_type() == sp2_tn.get_type():
        if sp1_tn.get_type() == tor_tn.get_type():
          # exact match
          return_dict['unification_matches'] = True
          return_dict['max_match_depth'] = current_depth
          return_dict['replace_dot_with_star'] = False
          if sp1_tn.get_num_siblings() == 0 and sp2_tn.get_num_siblings() == 0 and tor_tn.get_num_siblings() == 0:
            return_dict['match_type'] = p_consts.MATCH_TYPE_TES
          else:
            return_dict['match_type'] = p_consts.MATCH_TYPE_TEG
          return return_dict
        else:
          return_dict['unification_matches'] = False
          return_dict['max_match_depth'] = current_depth
          return_dict['replace_dot_with_star'] = False
          return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
          return return_dict

      # _val_ ph match
      return_dict['unification_matches'] = True
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_TV
      return return_dict

    # NT-NT-? (scope invariant)
    assert sp1_tn.is_nonterminal()
    assert sp2_tn.is_nonterminal()

    # NT-NT-T
    # NOTE not sure about this
    if tor_tn.is_terminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    # NT-NT-NT (scope invariant)
    assert tor_tn.is_nonterminal()

    # ./* ph match
    if sp1_tn.get_type() != sp2_tn.get_type():
      return_dict['unification_matches'] = True
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NTDS
      return return_dict

    # NT=NT?=NT (scope invariant)
    if sp1_tn.get_type() != tor_tn.get_type():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    # NOTE the most interesting part starts here
    # NT=NT=NT (scope invariant - types are identical)
    assert sp1_tn.get_type() == sp2_tn.get_type() == tor_tn.get_type()

    num_children_p1 = len(sp1_tn.get_children())
    num_children_p2 = len(sp2_tn.get_children())
    num_children_to = len(tor_tn.get_children())

    # NOTE at this point, all three nodes are non-terminals AND
    # their types are identical
    # check all combinations for number of children between p1 and p2 nodes
    if num_children_p1 == 1 and num_children_p2 == 1:

      # recurse down if all of three nodes have one child each
      if num_children_to == 1:
        return __rec_does_unification_match(
          sp1_tn.get_children()[0],
          sp2_tn.get_children()[0],
          tor_tn.get_children()[0],
          current_depth + 1
        )

      if sp1_tn.get_children()[0].get_type() == sp2_tn.get_children()[0].get_type():
        return_dict['unification_matches'] = False
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = False
        return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
        return return_dict

      # need to replace "." with "*"
      return_dict['unification_matches'] = True
      return_dict['max_match_depth'] = current_depth + 1
      return_dict['replace_dot_with_star'] = True
      return_dict['match_type'] = p_consts.MATCH_TYPE_NTDS
      return return_dict

    if num_children_p1 == 1 and num_children_p2 > 1:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    if num_children_p1 > 1 and num_children_p2 == 1:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    assert num_children_p1 > 1 and num_children_p2 > 1

    if num_children_p1 != num_children_p2:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    if num_children_p1 != num_children_to:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = p_consts.MATCH_TYPE_NOMATCH
      return return_dict

    # numch=numch=numch (scope invariant)
    children_can_match_vals = []
    children_max_match_depths = []
    children_should_replace_vals = []  # . with *
    children_match_types = []
    for p1_ch, p2_ch, to_ch in zip(sp1_tn.get_children(), sp2_tn.get_children(), tor_tn.get_children()):
      result_dict = __rec_does_unification_match(p1_ch, p2_ch, to_ch, current_depth+1)
      # sanity check
      for k, v in result_dict.items():
        assert v is not None, f'`{k}` of __rec_does_unification_match() is not set'
      children_can_match_vals.append(result_dict['unification_matches'])
      children_max_match_depths.append(result_dict['max_match_depth'])
      children_should_replace_vals.append(result_dict['replace_dot_with_star'])
      children_match_types.append(result_dict['match_type'])

    return_dict['unification_matches'] = all(children_can_match_vals)
    return_dict['max_match_depth'] = max(children_max_match_depths)
    return_dict['replace_dot_with_star'] = children_should_replace_vals
    return_dict['match_type'] = children_match_types
    return return_dict

  if is_insert_secret_fn:
    p1_tokens = sp1_tn.get_terminal_tokens()
    p2_tokens = sp2_tn.get_terminal_tokens()
    if p_consts.GENERIC_SECRET_FN in p1_tokens and p_consts.GENERIC_SECRET_FN in p2_tokens:
      # both should be only secret function invocation
      if len(p1_tokens) > 1 or len(p2_tokens) > 1:
        return {
          'unification_matches': False,
          'max_match_depth': 3,
          'replace_dot_with_star': False,
          'match_type': p_consts.MATCH_TYPE_NOMATCH
        }
      if p1_tokens[0] == p2_tokens[0] == p_consts.GENERIC_SECRET_FN:
        return {
          'unification_matches': True,
          'max_match_depth': 1,
          'replace_dot_with_star': False,
          'match_type': p_consts.MATCH_TYPE_TSEC
        }
      return {
        'unification_matches': False,
        'max_match_depth': 3,
        'replace_dot_with_star': False,
        'match_type': p_consts.MATCH_TYPE_NOMATCH
      }

  result_dict = __rec_does_unification_match(sp1_tn, sp2_tn, tor_tn, current_depth=1)
  return result_dict

def _calculate_match_penalty(templatized_node_match_types: list, match_penalty_coefs: Dict[str, float]) -> float:
  ''''''
  dict_counts = {}
  def __rec_count_types(tnmt: Union[list, str]):
    nonlocal dict_counts
    if isinstance(tnmt, str):
      dict_counts[tnmt] = dict_counts.get(tnmt, 0) + 1
      return
    assert isinstance(tnmt, list), f'expected list, found {type(tnmt)}'
    for elem in tnmt:
      __rec_count_types(elem)
  __rec_count_types(templatized_node_match_types)
  match_penalty = 1
  for match_type, penalty_coef in match_penalty_coefs.items():
    sign = 1 if penalty_coef >= 0 else -1
    match_penalty *= math.pow(abs(penalty_coef), sign * dict_counts.get(match_type, 0))

  return match_penalty

def _calculate_should_replace_penalty(should_replace_val: Union[bool, list]) -> float:
  '''
  N = count(True)
  M = count(False)
  return N / (N + M)
  '''
  true_count = 0
  false_count = 0
  def __rec_count(should_replace_val: Union[bool, list]) -> None:
    nonlocal true_count, false_count
    if isinstance(should_replace_val, bool):
      if should_replace_val: true_count += 1
      else: false_count += 1
      return
    assert isinstance(should_replace_val, list)
    for elem in should_replace_val:
      __rec_count(elem)
  __rec_count(should_replace_val)
  return true_count / (true_count + false_count)

def _has_repeating_tokens(sp1_tokens: Dict[int, List[str]], sp2_tokens: Dict[int, List[str]]) -> bool:
  '''
  sp_tokens = {
    node_id: List[token]
  }
  '''
  def __has_repeating_tokens(sp_tokens: Dict[int, List[str]]) -> bool:
    # NOTE check the node itself for repeating tokens
    # uncomment if this feature is not needed
    for node_id, tokens in sp_tokens.items():
      if len(tokens) != len(set(tokens)):
        return True

    node_ids = list(sp_tokens.keys())
    # iterate over pairs of tokens lists
    for i in range(0, len(node_ids) - 1):
      for j in range(i + 1, len(node_ids)):
        # check if any token from the first list appears in other lists
        for token in sp_tokens[node_ids[i]]:
          if token in sp_tokens[node_ids[j]]:
            return True
    return False
  return __has_repeating_tokens(sp1_tokens) or __has_repeating_tokens(sp2_tokens)


def val_sp1_tp1_candidates(
  sp1_tp1_cands: List[Dict[str, str]],
  contexts: List[dict],
  src_lang: str,
  tar_lang: str,
  **kwargs
):
  '''
  This function is invoked to check if the translation of the first
  program in source language is valid or not.

  CRITERIA:
  1. translation has no parse errors
  2. translation contains at least one context

  RETURN
  Program pairs that satisfy criteria
  '''
  _subject_name = kwargs['subject_name']
  logger.debug(f'{_subject_name} Starting validation of "SP1-TP1" candidates')

  return_dict = {}
  return_dict['good_program_pairs'] = []
  return_dict['success'] = False

  good_program_pairs = []
  for sp1_tp1_cand in sp1_tp1_cands:
    satisfies_criteria = _sp1_tp1_cand_satisfies_criteria(sp1_tp1_cand, contexts, src_lang, tar_lang, **kwargs)
    if satisfies_criteria:
      good_program_pairs.append(sp1_tp1_cand)

  if len(good_program_pairs) == 0:
    return return_dict

  return_dict['success'] = True
  return_dict['good_program_pairs'] = good_program_pairs
  return return_dict

def _sp1_tp1_cand_satisfies_criteria(
  sp1_tp1_cand: dict,
  contexts: dict,
  src_lang: str,
  tar_lang: str,
  **kwargs
) -> bool:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.debug(f'{_subject_name} Checking if SP1-TP1 candidate satisfies our criteria')

  sp1 = sp1_tp1_cand['source']
  tp1 = sp1_tp1_cand['target']

  # criteria 1
  if p_utils.does_have_parse_error(tp1, tar_lang):
    return False

  # criteria 2
  sp1_ast, _ = ast_parse.parse_text_dbg(sp1, src_lang)
  sp1_tree = pds.DuoGlotTree(sp1_ast)
  tp1_ast, _ = ast_parse.parse_text_dbg(tp1, tar_lang)
  tp1_tree = pds.DuoGlotTree(tp1_ast)

  all_contained_contexts = _get_all_contexts_contained(
    [sp1_tree],
    [tp1_tree],
    contexts
  )

  if len(all_contained_contexts) > 0:
    return True

  return False


def val_translation_pair_candidates(
  sp1: str,
  sp2: str,
  tp1_cand: str,
  tp2_cands: List[str],
  contexts: List[dict],
  src_lang: str,
  tar_lang: str,
  **kwargs
):
  '''
  This function is invoked to check if the translation pair
  is valid

  CRITERIA:
  1. translation candidate of SP2 has no parse errors
  2. translation candidates of SP1 and SP2 are type-isomorphic
  except at identifiers and literals
  3. translation candidate of SP2 contains the same context as SP1

  RETURN
  All candidate translations that satisfy criteria
  '''
  _subject_name = kwargs['subject_name']
  logger.debug(f'{_subject_name} Starting validation of "Translation Pair" candidates')

  return_dict = {}
  return_dict['translation_pairs'] = []
  return_dict['success'] = False

  for tp2_cand in tp2_cands:
    sp2_translation_is_good = _tp2_candidate_satisfies_criteria(
      sp1,
      sp2,
      tp1_cand,
      tp2_cand,
      contexts,
      src_lang,
      tar_lang,
      **kwargs
    )
    if sp2_translation_is_good:
      return_dict['translation_pairs'].append([
        {'source': sp1, 'target': tp1_cand},
        {'source': sp2, 'target': tp2_cand},
      ])

  if len(return_dict['translation_pairs']) > 0:
    return_dict['success'] = True

  return return_dict

def _tp2_candidate_satisfies_criteria(
  sp1: str,
  sp2: str,
  tp1_cand: str,
  tp2_cand: str,
  contexts: dict,
  src_lang: str,
  tar_lang: str,
  **kwargs
) -> bool:
  ''''''
  _subject_name = kwargs['subject_name']
  logger.debug(f'{_subject_name} Checking if TP2 candidate satisfies our criteria')

  # criteria 1
  if p_utils.does_have_parse_error(tp2_cand, tar_lang):
    return False

  # criteria 2
  are_targets_type_isomorphic = _are_translations_identical_except_identifiers(
    tp1_cand,
    tp2_cand,
    src_lang,
    tar_lang
  )
  if not are_targets_type_isomorphic:
    return False

  # criteria 3
  source_trees : List[pds.DuoGlotTree] = []
  for source in [sp1, sp2]:
    source_ast, _ = ast_parse.parse_text_dbg(source, src_lang)
    source_tree = pds.DuoGlotTree(source_ast)
    source_trees.append(source_tree)
  target_trees : List[pds.DuoGlotTree] = []
  for target in [tp1_cand, tp2_cand]:
    target_ast, _ = ast_parse.parse_text_dbg(target, tar_lang)
    target_tree = pds.DuoGlotTree(target_ast)
    target_trees.append(target_tree)

  contexts_contained = _get_all_contexts_contained(source_trees, target_trees, contexts)
  if len(contexts_contained) == 0:
    return False

  return True

def _are_translations_identical_except_identifiers(
  trans1: str,
  trans2: str,
  src_lang: str,
  tar_lang: str
):
  '''
  Two translations (programs in the target language) are identical iff
  1. The trees are type isomorphic (refer to `is_generated_code_type_isomorphic_to_template_origin`)
  2. All terminals EXCEPT identifiers are identical

  PRE1: trans1 does not have parse errors
  PRE2: trans2 does not have parse errors

  TODO hard-coded to JavaScript
  '''

  trans1_ast, _ = ast_parse.parse_text_dbg(trans1, tar_lang)
  trans2_ast, _ = ast_parse.parse_text_dbg(trans2, tar_lang)
  trans1_tree = pds.DuoGlotTree(trans1_ast)
  trans2_tree = pds.DuoGlotTree(trans2_ast)

  trans1_enc = _get_type_ahu_ter_x_ident_encoding(trans1_tree)
  trans2_enc = _get_type_ahu_ter_x_ident_encoding(trans2_tree)

  are_compatible = trans1_enc == trans2_enc

  return are_compatible

def _get_type_ahu_ter_x_ident_encoding(tree: pds.DuoGlotTree) -> str:
  '''
  Compute AHU encoding with
  1. type information
  2. terminals except identifiers
  3. terminals except literals
  for comparing tree for type-isomorphism
  https://www.baeldung.com/cs/isomorphic-trees#1-ahu-encoding
  '''

  def __rec_post_order(node: pds.DuoGlotNode):
    if isinstance(node, pds.TNode):
      return node.get_type()

    if node.is_terminal():
      if node.get_num_siblings() == 0:
        return '0'
    if node.has_single_terminal_child():
      return '0'

    children_encoding = ''
    for child in node.get_children():
      children_encoding += __rec_post_order(child)
    return f'({node.get_type()} {children_encoding})'

  return __rec_post_order(tree.get_root_node())

def _get_type_ahu_encoding_x_ident(tree: pds.DuoGlotTree) -> str:
  '''
  Compute AHU encoding with
  1. type information
  2. all terminals except identifier and literal terminals
  for removing duplicates of TSP candidates
  https://www.baeldung.com/cs/isomorphic-trees#1-ahu-encoding
  '''
  def __rec_post_order(node: pds.DuoGlotNode) -> str:
    if node.is_terminal():
      if node.get_num_siblings() == 0:  # identifier or literal
        return '0'
      else:
        return node.get_type()
    children_encoding = ''
    for child in node.get_children():
      children_encoding += __rec_post_order(child)
    return f'({node.get_type()} {children_encoding})'

  return __rec_post_order(tree.get_root_node())


def _is_generated_code_type_isomorphic_to_shallow_template(
  gen_tree: pds.DuoGlotTree,
  template_tree: pds.DuoGlotTree,
  templatized_node_paths: List[List[int]]
) -> bool:
  '''
  everything except templatized nodes (holes) is the same
  templatized nodes can be arbitrarily different
  NOTE refer to notes or update this doc
  TODO what does `shallow template` mean?
  '''

  gen_type_enc = _get_tree_encoding_except_templatized_nodes(gen_tree, templatized_node_paths)
  if gen_type_enc is None:
    return False
  template_type_enc = _get_tree_encoding_except_templatized_nodes(template_tree, templatized_node_paths)
  assert template_type_enc is not None, 'should not happen: templatized_node_ids are invalid'

  return gen_type_enc == template_type_enc

def _get_tree_encoding_except_templatized_nodes(
  tree: pds.DuoGlotTree,
  templatized_node_paths: List[List[int]]
) -> Union[str, None]:
  '''
  Get string encoding of a tree
  Return None if any of templatized nodes is missing from tree
  TODO update this doc
  '''
  def __rec_post_order(node: pds.DuoGlotNode):
    nonlocal templatized_nodes
    if node in templatized_nodes:
      return '__'
    if isinstance(node, pds.TNode):
      return node.get_type()
    children_encoding = ''
    for child in node.get_children():
      children_encoding += __rec_post_order(child)
    return f'{node.get_type()} ({children_encoding})'

  root_node = tree.get_root_node()

  # get_child_by_path() relative to context node
  # context node should be the only child when its text is parsed as it is
  # TODO this may need refactoring
  if len(root_node.get_children()) != 1:
    return None

  context_node = root_node.get_children()[0]
  templatized_nodes = [context_node.get_child_by_path(path) for path in templatized_node_paths]

  if any(map(lambda node: node is None, templatized_nodes)):
    return None

  return __rec_post_order(tree.get_root_node())

def _get_all_contexts_contained(
  source_trees: List[pds.DuoGlotTree],
  target_trees: List[pds.DuoGlotTree],
  contexts: list,
):
  ''''''
  contexts_contained = []
  for context in contexts:
    ctx_exists = _context_exists(source_trees, target_trees, context['source_context'], context['target_context'])
    if ctx_exists:
      contexts_contained.append(context)
  return contexts_contained

def _context_exists(
  src_trees: List[pds.DuoGlotTree],
  tar_trees: List[pds.DuoGlotTree],
  src_ctx: list,
  tar_ctx: list,
) -> bool:
  '''
  Implementation of this function is similar to p_post_process_translation_rule.TranslationRule.trim_context()
  '''

  def __are_previous_siblings(node: pds.DuoGlotNode, sibling_types: List[str]) -> bool:
    '''
    PRE: siblings are ordered naturally (as appeared in tree)

    IDEA
    Get all NT siblings to the left, make 1-1 comparison
    '''
    assert isinstance(node, pds.DuoGlotNode)
    node_siblings = node.get_siblings_to_the_left()

    # we only need non-terminal nodes
    node_siblings = list(filter(lambda x: x.is_nonterminal(), node_siblings))

    # base case 2
    if len(node_siblings) != len(sibling_types):
      return False

    # TODO since templates can be simplified, it may ever so happen that previous sibling nodes
    # of problematic node get simplified. In this case, sibling node type changes from
    # the one in original template to a node type that replaces it. Thus,
    # the check below cannot find the right context for it.
    # Workaround is to check the number of previous siblings. In the future, the number of
    # siblings may depend on whether the matcher is '*' or '.'.
    # for node_sibling, sibling_type in zip(node_siblings, reversed(sibling_types)):
    #   if node_sibling.get_type().strip('"') != sibling_type.strip('"'):
    #     return False
    if len(node_siblings) != len(sibling_types):
      return False

    return True

  def __are_parents(node: pds.DuoGlotNode, parent_types: List[str]) -> bool:
    '''
    PRE: siblings are ordered naturally (as appeared in tree)

    IDEA
    Starting from immediate parent, go up until reach root node OR
    exhaust parent_types, make 1-1 comparison
    '''
    assert isinstance(node, pds.DuoGlotNode)

    cursor_node = node.get_parent()
    parent_type_idx = 0

    while True:

      # stop condition 1
      if cursor_node is None:
        break

      # stop condition 2
      if parent_type_idx == len(parent_types):
        break

      parent_type = parent_types[parent_type_idx]
      if cursor_node.get_type().strip('"') != parent_type.strip('"'):
        return False

      parent_type_idx += 1
      cursor_node = cursor_node.get_parent()

    # there is a parent_type that we did not check
    if parent_type_idx < len(parent_types):
      return False

    return True

  def __rec_pre_order_find_node_under_context(
    node: pds.DuoGlotNode,
    sibling_types: List[str],
    parent_types: List[str]
  ) -> Union[pds.DuoGlotNode, None]:
    '''
    Return the earliest occurence of the node
    '''
    if isinstance(node, pds.TNode):
      return None

    is_siblings_ok = __are_previous_siblings(node, sibling_types)
    is_parents_ok = __are_parents(node, parent_types)
    if is_siblings_ok and is_parents_ok:
      return node

    # TODO why do we have this if statement?
    if node.has_single_terminal_child():
      return None

    for child_node in node.get_children():
      child_result = __rec_pre_order_find_node_under_context(child_node, sibling_types, parent_types)
      if child_result is not None:
        return child_result

    return None

  def __get_node_under_context(root_node: pds.DuoGlotNode, siblings: list, parents: list) -> pds.DuoGlotNode:
    ''''''
    node_under_context = __rec_pre_order_find_node_under_context(root_node, siblings, parents)
    return node_under_context

  for src_tree in src_trees:
    src_problematic_node = __get_node_under_context(src_tree.get_root_node(), src_ctx['siblings'], src_ctx['parents'])
    if src_problematic_node is None:
      return False

  for tar_tree in tar_trees:
    tar_problematic_node = __get_node_under_context(tar_tree.get_root_node(), tar_ctx['siblings'], tar_ctx['parents'])
    if tar_problematic_node is None:
      return False

  return True


def _test_val_simplified_template_candidates():
  template_fpath = Path('/code/repo-duoglot/backend/duoglotcore-server/pirel-logs/02-08-04-56-15.842895-TEMPLATE_p_pirel.json')
  simplified_template_candidates_fpath = Path('/code/repo-duoglot/backend/duoglotcore-server/pirel-logs/02-08-04-56-39.368370-st-cand-code-blocks.json')

  template_dict = p_utils.read_json(template_fpath)
  st_cands = p_utils.read_json(simplified_template_candidates_fpath)

  src_lang = template_dict['src_lang']
  template_origin = template_dict['template_origin']
  templatized_node_ids_context = template_dict['templatized_node_ids_context']

  kwargs = {
    'subject_name': 'test-templ-cands'
  }

  val_result_dict = val_simplified_template_candidates(src_lang, template_origin, templatized_node_ids_context, st_cands, **kwargs)
  p_utils.write_json('temporary_test_val_simplified_template_candidates.json', val_result_dict)

def _test_val_tsp_candidates():
  test_harness_config:dict = p_utils.read_json('temporary_test_val_tsp_candidates_config.json')
  simplified_template_fpath = Path(test_harness_config['stp'])
  generated_code_blocks_fpath = Path(test_harness_config['gcp'])

  template_dict = p_utils.read_json(simplified_template_fpath)
  generated_code_blocks = test_harness_config.get(
    'generated_code_blocks',
    p_utils.read_json(generated_code_blocks_fpath)
  )

  src_lang = template_dict['src_lang']
  template_origin = template_dict['template_origin']
  templatized_node_ids = template_dict['templatized_node_ids']
  is_insert_secret_fn = template_dict['is_insert_secret_fn']

  kwargs = {
    'subject_name': 'test-val-tsp-cands'
  }

  val_result_dict = val_tsp_candidates(src_lang, template_origin, templatized_node_ids, generated_code_blocks, is_insert_secret_fn, **kwargs)
  p_utils.write_json('temporary_test_val_tsp_candidates.json', val_result_dict)

  from p_llm_gen import _get_best_n_tsps
  program_pairs, templatized_nodes_replace_dot_w_star_flags = _get_best_n_tsps(
    val_result_dict['valid_tsp_lists_sorted'],
    val_result_dict['num_candidate_tsps_filtered']
  )
  p_utils.write_json('temporary_test_val_tsp_candidates_TSPs.json', program_pairs)

def _test_val_sp1_tp1_candidates():
  test_harness_config:dict = p_utils.read_json('temporary_test_val_sp1_tp1_candidates_config.json')
  simplified_template_fpath = Path(test_harness_config['simplified_template_fpath'])
  tp1_candidates_fpath = Path(test_harness_config['tp1_candidates_fpath'])
  best_n_tsps_fpath = Path(test_harness_config['best_n_tsps_fpath'])

  template_dict = p_utils.read_json(simplified_template_fpath)
  tp1_candidates = p_utils.read_json(tp1_candidates_fpath)
  best_n_tsps = p_utils.read_json(best_n_tsps_fpath)

  src_lang = template_dict['src_lang']
  tar_lang = template_dict['tar_lang']
  contexts = template_dict['contexts']

  kwargs = {
    'subject_name': 'test-val-sp1-tp1-cands'
  }

  for i, tsp in enumerate(best_n_tsps):
    sp1 = tsp[0]
    sp1_tp1_cands = [{'source': sp1, 'target': tp1_cand} for tp1_cand in tp1_candidates]
    val_result_dict = val_sp1_tp1_candidates(sp1_tp1_cands, contexts, src_lang, tar_lang, **kwargs)
    p_utils.write_json(f'temporary_test_val_sp1_tp1_candidates_{i}.json', val_result_dict)

def _test_val_translation_pair_candidates():
  simplified_template_fpath = Path('/code/repo-duoglot/backend/duoglotcore-server/pirel-logs/debug-03-ZeroTranslationPairsException/02-09-07-16-03.696413-simplified-TEMPLATE-p_llm_gen.json')
  template_dict = p_utils.read_json(simplified_template_fpath)

  src_lang = template_dict['src_lang']
  tar_lang = template_dict['tar_lang']
  contexts = template_dict['contexts']

  sp1 = 'midVal1 = nums1[i] if i < j else 0'
  sp2 = 'midVal1 = nums1[i] if 1 < 2 else 0'

  tp1_cand = 'midVal1 = i < j ? pirel_dummy_var : Infinity;'
  tp2_cands = [
    'midVal1 = 1 < 2 ? pirel_dummy_var : Infinity;'
  ]

  kwargs = {
    'subject_name': 'test-val-transpair-cands'
  }

  val_result_dict = val_translation_pair_candidates(sp1, sp2, tp1_cand, tp2_cands, contexts, src_lang, tar_lang, **kwargs)
  p_utils.write_json('temporary_test_val_translation_pair_candidates.json', val_result_dict)

if __name__ == '__main__':
  # _test_val_simplified_template_candidates()
  _test_val_tsp_candidates()
  # _test_val_translation_pair_candidates()
  # _test_val_sp1_tp1_candidates()
