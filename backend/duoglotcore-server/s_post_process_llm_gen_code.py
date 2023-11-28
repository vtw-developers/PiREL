'''
A module for post-processing LLM generated code like:
1. Parsing and checking the code against the template that was used to generate it.
2. Parsing and checking LLM translations
'''

from s_data_structures import *
from s_parse_utils import PY_LANGUAGE, JS_LANGUAGE, has_parse_error
from tree_sitter import Parser
import ast_parse
import ast_match
from typing import List, Dict
import random
import math


# ==============================================================================
# ================= POST-PROCESSING SIMPLIFIED TEMPLATES =======================
# ==============================================================================
def post_process_simplified_templates(
  data_to_postprocess: dict
) -> dict:
  '''
  Simplified templates should satisfy the following criteria:
  1. Should be parseable
  2. Everything except templatized nodes should be identical to template origin
  3. Simplest AST at templatized nodes.
  How do we measure simplicity? Should not exceed depth N.
  '''

  MAX_DEPTH = 4

  lang = data_to_postprocess['lang']
  template_origin = data_to_postprocess['template_origin']
  templatized_node_ids_context = data_to_postprocess['templatized_node_ids_context']
  simplified_templates = data_to_postprocess['simplified_templates']

  return_data = {}
  return_data['simplified_templates_stats'] = []

  # 1 get the stats for simplified templates
  for i, simplified_template in enumerate(simplified_templates):
    result_dict = _post_process_simplified_template(
      simplified_template,
      template_origin,
      templatized_node_ids_context,
      lang
    )
    return_data['simplified_templates_stats'].append([i, result_dict])

  # 2 filter programs that satisfy our criteria
  return_data['simplest_template'] = None
  return_data['templatized_node_texts'] = None
  max_overall_depth = 1e10
  for i, sim_templ_stats in return_data['simplified_templates_stats']:
    if sim_templ_stats['has_parse_error']:
      continue
    if not sim_templ_stats['is_type_isomorphic_to_template_origin']:
      continue
    depths = sim_templ_stats['depths_at_templatized_nodes']
    if not all(map(lambda depth: depth <= MAX_DEPTH, depths)):
      continue
    if sum(depths) < max_overall_depth:
      return_data['simplest_template'] = sim_templ_stats['simplified_template']
      return_data['templatized_node_texts'] = sim_templ_stats['texts_at_templatized_nodes']
      max_overall_depth = sum(depths)

  return return_data


def _post_process_simplified_template(
  simplified_template: str,
  template_origin: str,
  templatized_node_ids_context: dict,
  lang: str
):
  ''''''
  assert lang == 'py'

  parser = Parser()
  parser.set_language(PY_LANGUAGE)

  return_data = {}
  return_data["template_origin"] = template_origin
  return_data["simplified_template"] = simplified_template
  return_data["has_parse_error"] = None
  return_data["is_type_isomorphic_to_template_origin"] = None
  return_data["depths_at_templatized_nodes"] = []
  return_data["texts_at_templatized_nodes"] = []

  # check for criteria #1 - parse error
  return_data["has_parse_error"] = has_parse_error(simplified_template, parser=parser)

  if return_data["has_parse_error"]:
    return return_data

  # check for criteria #2 - type isomorphism with template
  templatized_node_paths = list(templatized_node_ids_context.values())
  simplified_template_ast_text, _ = ast_parse.parse_text_dbg_keep_text(simplified_template, lang)
  template_origin_ast_text, _ = ast_parse.parse_text_dbg_keep_text(template_origin, lang)

  simplified_template_tree = PirelTree(simplified_template_ast_text)
  template_origin_tree = PirelTree(template_origin_ast_text)

  return_data["is_type_isomorphic_to_template_origin"] = _is_generated_code_type_isomorphic_to_shallow_template_v3(
    simplified_template_tree,
    template_origin_tree,
    templatized_node_paths
  )

  if not return_data["is_type_isomorphic_to_template_origin"]:
    return return_data

  # check for criteria #3 - collect depths of templatized nodes
  simplified_template_tree._fix_indentation()
  root_node = simplified_template_tree.get_root_node()

  if len(root_node.get_children()) != 1:
    return return_data

  for templatized_node_path in templatized_node_paths:
    context_node = root_node.get_children()[0]
    templatized_node = context_node.get_child_by_path(templatized_node_path)
    tn_depth = templatized_node.get_depth()
    tn_text = templatized_node.get_text()
    return_data["depths_at_templatized_nodes"].append(tn_depth)
    return_data["texts_at_templatized_nodes"].append(tn_text)

  return return_data


# ==============================================================================
# ================= POST-PROCESSING GENERATED CODE =============================
# ==============================================================================

def post_process_generated_code_blocks(
  data_to_postprocess: dict
) -> List[dict]:
  '''
  Post-process a list of generated code blocks.
  Do not return candidate programs.

  return_data = {
    generated_codes_stats: [],
    num_progs_satisfy_criteria: int,
    unique_post_processed_programs: List[str],
    num_unique_post_processed_programs: int
  }

  CRITERIA
  1. no parse error
  2. is type-isomorphic to template everywhere except templatized nodes
  3. at templatized nodes TODO update later

  UNIQUENESS
  Compare string-serialized versions of trees.
  We don't need identical generated programs,
  since duplicates are redundant.
  '''

  lang : str = data_to_postprocess['lang']
  template_origin : str = data_to_postprocess['template_origin']
  templatized_node_ids : dict = data_to_postprocess['templatized_node_ids']
  generated_code_blocks : list = data_to_postprocess['generated_code_blocks']

  return_data = {}
  return_data['generated_codes_stats'] = []

  # 1 get the stats for generated blocks of code
  for i, generated_code in enumerate(generated_code_blocks):
    result_dict = _post_process_generated_code(
      generated_code,
      template_origin,
      templatized_node_ids,
      lang
    )
    return_data['generated_codes_stats'].append([i, result_dict])

  # 2 filter programs that satisfy our criteria
  filtered_programs = []
  for i, gen_code_stats in return_data['generated_codes_stats']:
    if gen_code_stats['has_parse_error']:
      continue
    if not gen_code_stats['is_type_isomorphic_to_template']:
      continue
    if not gen_code_stats['templatized_nodes_depth_lte_2']:
      continue
    filtered_programs.append(gen_code_stats['generated_code'])
  return_data['num_progs_satisfy_criteria'] = len(filtered_programs)

  # 3 select unique programs
  unique_program_encodings = []
  unique_programs = []
  for prog in filtered_programs:
    prog_ser = _get_tree_serialize_as_str(prog)
    if prog_ser not in unique_program_encodings:
      unique_program_encodings.append(prog_ser)
      unique_programs.append(prog)
  return_data['unique_post_processed_programs'] = unique_programs
  return_data['num_unique_post_processed_programs'] = len(unique_programs)

  return return_data


def post_process_generated_code_blocks_v2(
  data_to_postprocess: dict
) -> List[dict]:
  '''
  post-process to return two programs in source language that are
  1. no parse errors
  2. identical to template except at templatized nodes
  3. at templatized nodes, max depth is 2
  4. no repeating tokens across all templatized nodes

  we assume that the template is filled with literals and identifiers
  '''

  lang : str = data_to_postprocess['lang']
  template_origin : str = data_to_postprocess['template_origin']
  templatized_node_ids : dict = data_to_postprocess['templatized_node_ids']
  generated_code_blocks : list = data_to_postprocess['generated_code_blocks']

  return_data = {}
  return_data['generated_codes_stats'] = []
  return_data['two_source_programs'] = []
  return_data['success'] = False

  # 1 get the stats for generated blocks of code
  for i, generated_code in enumerate(generated_code_blocks):
    result_dict = _post_process_generated_code(
      generated_code,
      template_origin,
      templatized_node_ids,
      lang
    )
    return_data['generated_codes_stats'].append([i, result_dict])

  # 2 filter programs that satisfy our criteria (1-3)
  filtered_programs = []
  for i, gen_code_stats in return_data['generated_codes_stats']:
    if gen_code_stats['has_parse_error']:
      continue
    if not gen_code_stats['is_type_isomorphic_to_template']:
      continue
    if not gen_code_stats['templatized_nodes_depth_lte_2']:
      continue
    filtered_programs.append(gen_code_stats['generated_code'])
  return_data['num_progs_satisfy_criteria'] = len(filtered_programs)

  # 3 select two programs such that templatized nodes have different tokens
  if len(filtered_programs) < 2:
    return_data['two_source_programs'] = filtered_programs
    return_data['success'] = False
    return return_data

  for i in range(len(filtered_programs) - 1):
    for j in range(i + 1, len(filtered_programs)):
      program1 = filtered_programs[i]
      program2 = filtered_programs[j]
      is_pair_compatible = _templatized_nodes_have_different_tokens(
        program1,
        program2,
        list(templatized_node_ids.values())
      )
      if is_pair_compatible:
        return_data['two_source_programs'] = [program1, program2]
        return_data['success'] = True
        return return_data

  return return_data


def _post_process_generated_code(
  generated_code: str,
  template_origin: str,
  templatized_node_ids: dict,
  lang: str
) -> dict:
  '''
  Given a single generated program and its template origin

  TERMS:
  generated_code - a single program generated by LLM by filling holes in a template.
  template_origin - a piece of code from which the template was generated.
  templatized_node_ids - path to templatized nodes and their ids
  lang - a short representation of a programming language (e.g. py, js, etc)
  MAX_DEPTH - max depth for nodes at templatized nodes

  RETURN FORMAT
  returnData = {
    generated_code: str
    template_origin: str,
    has_parse_error: bool,
    is_type_isomorphic_to_template: bool,
  }
  '''

  # NOTE hard-coded to be Python temporarily
  assert lang == "py"

  MAX_DEPTH = 3

  parser = Parser()
  parser.set_language(PY_LANGUAGE)

  return_data = {}
  return_data["template_origin"] = template_origin
  return_data["generated_code"] = generated_code
  return_data["has_parse_error"] = None
  return_data["is_type_isomorphic_to_template"] = None
  return_data["templatized_nodes_depth_lte_2"] = None

  # check for criteria #1 - parse error
  return_data["has_parse_error"] = has_parse_error(generated_code, parser=parser)
  if return_data["has_parse_error"]:
    return return_data

  # check for criteria #2 - type isomorphism with template
  templatized_node_paths = list(templatized_node_ids.values())
  generated_code_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, generated_code, lang)
  template_origin_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, template_origin, lang)

  generated_code_tree = DuoGlotTree(generated_code_ast)
  template_origin_tree = DuoGlotTree(template_origin_ast)

  return_data["is_type_isomorphic_to_template"] = _is_generated_code_type_isomorphic_to_shallow_template_v3(
    generated_code_tree,
    template_origin_tree,
    templatized_node_paths
  )

  return_data["templatized_nodes_depth_lte_2"] = _check_templatized_nodes_depths(
    generated_code_tree,
    templatized_node_paths,
    max_depth=MAX_DEPTH
  )

  return return_data


# current implementation
def post_process_generated_code_blocks_v3(
  data_to_postprocess: dict
) -> List[dict]:
  '''
  Post-process to return two programs in source language that are
  1. no parse errors
  2. identical to template except at templatized nodes (a.k.a is_type_isomorphic_to_template)
  3. at templatized nodes ((a xor b) and c and d):
    a. string of NT-NT-T nodes of width 1 (includes max_depth=2) (guarantees single T token)
    b. different node types (doesn't guarantee single T token)
    c. no repeating tokens (may conflict with {b})
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

  def _program_pair_min_penalty(filtered_program_pairs: List[dict]) -> dict:
    '''min penalty is the best'''
    assert len(filtered_program_pairs) > 0
    min_penalty = filtered_program_pairs[0]['pair_penalty']
    best_pp = filtered_program_pairs[0]
    for fpp in filtered_program_pairs[1:]:
      if fpp['pair_penalty'] < min_penalty:
        min_penalty = fpp['pair_penalty']
        best_pp = fpp
    return best_pp

  def _sorted_filtered_program_pairs_by_penalty(filtered_program_pairs: List[dict]) -> List[dict]:
    '''min penalty is the best'''
    assert len(filtered_program_pairs) > 0
    sorted_program_pairs = sorted(filtered_program_pairs, key=lambda tsps: tsps['pair_penalty'])
    return sorted_program_pairs

  lang : str = data_to_postprocess['lang']
  template_origin : str = data_to_postprocess['template_origin']
  templatized_node_ids : dict = data_to_postprocess['templatized_node_ids']
  generated_code_blocks : list = data_to_postprocess['generated_code_blocks']
  is_insert_secret_fn : bool = data_to_postprocess['is_insert_secret_fn']

  return_dict = {}
  return_dict['generated_codes_stats'] = []
  return_dict['two_source_programs_stats'] = []
  return_dict['success'] = None
  return_dict['valid_tsp_list'] = None

  # 1 get the stats for generated blocks of code
  for i, generated_code in enumerate(generated_code_blocks):
    result_dict = _post_process_generated_code_v3(
      generated_code,
      template_origin,
      templatized_node_ids,
      lang
    )
    return_dict['generated_codes_stats'].append([i, result_dict])

  # 2 filter programs that satisfy our criteria (1-2)
  filtered_programs = []
  for i, gen_code_stats in return_dict['generated_codes_stats']:
    if gen_code_stats['has_parse_error']:
      continue
    if not gen_code_stats['is_type_isomorphic_to_template']:
      continue
    filtered_programs.append(gen_code_stats['generated_code'])

  # not enough programs for pairs
  if len(filtered_programs) < 2:
    return_dict['success'] = False
    return return_dict

  # 3 iterate over all possible pairs and collect analysis
  for i in range(len(filtered_programs) - 1):
    for j in range(i + 1, len(filtered_programs)):
      program1 = filtered_programs[i]
      program2 = filtered_programs[j]
      two_source_programs_analysis_results = _post_process_two_source_programs_v3(
        lang,
        program1,
        program2,
        template_origin,
        templatized_node_ids,
        is_insert_secret_fn
      )
      return_dict['two_source_programs_stats'].append(two_source_programs_analysis_results)

  # 4 analyze the pairs
  filtered_program_pairs = []
  for tsp_stat in return_dict['two_source_programs_stats']:
    if not tsp_stat['all_templatized_nodes_match']:
      continue
    if not tsp_stat['no_repeating_tokens']:
      continue
    filtered_program_pairs.append(tsp_stat)

  # this signals to query LLM again
  if len(filtered_program_pairs) == 0:
    return_dict['success'] = False
    return return_dict

  # best available program pair
  bapp = _program_pair_min_penalty(filtered_program_pairs)
  return_dict['success'] = True
  return_dict['min_penalty'] = bapp['pair_penalty']

  # all valid program pairs sorted by score (if the best doesn't work)
  # NOTE we need this, because the best program pair may not be easy to translate to target language
  return_dict['valid_tsp_list'] = _sorted_filtered_program_pairs_by_penalty(filtered_program_pairs)

  return return_dict


def _post_process_generated_code_v3(
  generated_code: str,
  template_origin: str,
  templatized_node_ids: dict,
  lang: str
) -> dict:
  '''
  Given a single generated program and its template origin

  TERMS:
  generated_code - a single program generated by LLM by filling holes in a template.
  template_origin - a piece of code from which the template was generated.
  templatized_node_ids - path to templatized nodes and their ids
  lang - a short representation of a programming language (e.g. py, js, etc)
  MAX_DEPTH - max depth for nodes at templatized nodes

  RETURN FORMAT
  returnData = {
    generated_code: str
    template_origin: str,
    has_parse_error: bool,
    is_type_isomorphic_to_template: bool,
  }
  '''

  # NOTE hard-coded to be Python temporarily
  assert lang == "py"

  parser = Parser()
  parser.set_language(PY_LANGUAGE)

  return_data = {}
  return_data["template_origin"] = template_origin
  return_data["generated_code"] = generated_code
  return_data["has_parse_error"] = None
  return_data["is_type_isomorphic_to_template"] = None

  # check for criteria #1 - parse error
  return_data["has_parse_error"] = has_parse_error(generated_code, parser=parser)
  if return_data["has_parse_error"]:
    return return_data

  # check for criteria #2 - type isomorphism with template
  templatized_node_paths = list(templatized_node_ids.values())
  generated_code_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, generated_code, lang)
  template_origin_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, template_origin, lang)

  generated_code_tree = DuoGlotTree(generated_code_ast)
  template_origin_tree = DuoGlotTree(template_origin_ast)

  return_data["is_type_isomorphic_to_template"] = _is_generated_code_type_isomorphic_to_shallow_template_v3(
    generated_code_tree,
    template_origin_tree,
    templatized_node_paths
  )

  return return_data


def _post_process_two_source_programs_v3(
  lang: str,
  program1: str,
  program2: str,
  template_origin: str,
  templatized_node_ids: dict,
  is_insert_secret_fn: bool
) -> dict:
  '''
  INTERNAL
  pair_penalty - a value that is used for ranking pairs of programs
  in source language. The smaller the value, the better the pair.

  NOTES
  1. All templatized nodes at program1 and program2, when unified,
  should match a templatized node at template origin.

  RETURN
  do all nodes match when unified? score for the pair
  '''

  # TODO optimize: use previously parsed trees
  program1_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, program1, lang)
  program2_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, program2, lang)
  template_origin_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, template_origin, lang)

  program1_tree = DuoGlotTree(program1_ast)
  program2_tree = DuoGlotTree(program2_ast)
  template_origin_tree = DuoGlotTree(template_origin_ast)

  templatized_nodes_can_match_values = []
  templatized_nodes_penalties = []
  templatized_nodes_should_replace_values = []
  templatized_nodes_match_types = []
  all_tokens = []
  count_template_nodes_width_1 = 0

  # iterate over templatized nodes
  for node_id, path_to_templatized_node in templatized_node_ids.items():

    # TODO it looks like we don't need this information,
    # since we already have the template_origin
    # templatized_node_ast_origin = templatized_node_ids_types[node_id]

    # 1 get templatized nodes at node_id
    p1_tn = _get_templatized_node_v3(program1_tree, path_to_templatized_node)
    p2_tn = _get_templatized_node_v3(program2_tree, path_to_templatized_node)
    to_tn = _get_templatized_node_v3(template_origin_tree, path_to_templatized_node)

    # NOTE should_replace does not consider multiple ph nodes under a template node
    result_dict = _unification_of_template_nodes_can_match_v4(p1_tn, p2_tn, to_tn, is_insert_secret_fn)
    can_match = result_dict['unification_matches']
    max_match_depth = result_dict['max_match_depth']
    should_replace = result_dict['replace_dot_with_star']
    match_types = result_dict['match_type']

    templatized_nodes_can_match_values.append(can_match)
    templatized_nodes_should_replace_values.append(should_replace)
    templatized_nodes_match_types.append(match_types)

    # 2 get score for the current templatized node
    p1_T_tokens = p1_tn.get_terminal_tokens()
    p2_T_tokens = p2_tn.get_terminal_tokens()
    num_tokens = (len(p1_T_tokens) + len(p2_T_tokens)) / 2
    multiple_token_penalty = 1
    if abs(num_tokens - 1) > 1e-20:  # num_tokens > 1
      multiple_token_penalty = 2

    # penalize "." to "*" conversions
    # the idea is to keep dots as much as possible
    should_replace_penalty = 20 if should_replace else 1

    # less is better
    templatized_node_penalty = max_match_depth * multiple_token_penalty * num_tokens * should_replace_penalty
    templatized_nodes_penalties.append(templatized_node_penalty)

    # 3 tokens
    all_tokens.extend(p1_T_tokens)
    all_tokens.extend(p2_T_tokens)

    # 4 check for string of NT-NT-T nodes of width 1
    count_template_nodes_width_1 += int(p1_tn.is_ast_width_1())
    count_template_nodes_width_1 += int(p2_tn.is_ast_width_1())

  # tree edit distance between two source programs
  # TODO finish implementation
  # we don't need it for now
  # te_dist = _tree_edit_distance(program1_tree, program2_tree)

  # match penalty
  match_penalty = _calculate_match_penalty(templatized_nodes_match_types)

  # sum of squares
  pair_penalty = sum([penalty * match_penalty for penalty in templatized_nodes_penalties])
  all_templatized_nodes_match = all(templatized_nodes_can_match_values)
  ratio_template_nodes_width_1 = count_template_nodes_width_1 / (2 * len(templatized_node_ids))

  # NOTE no repeating tokens can be false iff the holes are filled with single tokens
  # forcing this condition otherwise on complex hole fills is too restrictive
  no_repeating_tokens = True
  if len(all_tokens) == len(templatized_node_ids) * 2:
    no_repeating_tokens = len(set(all_tokens)) == len(all_tokens)

  return_dict = {
    'program1': program1,
    'program2': program2,
    'pair_penalty': pair_penalty,
    'all_templatized_nodes_match': all_templatized_nodes_match,
    'no_repeating_tokens': no_repeating_tokens,
    'ratio_template_nodes_width_1': ratio_template_nodes_width_1,
    'templatized_nodes_replace_dot_w_star_flags': templatized_nodes_should_replace_values,
    'templatized_nodes_match_types': templatized_nodes_match_types,
    'match_penalty': match_penalty
  }

  return return_dict


def _get_templatized_node_v3(tree: DuoGlotTree, path: List[int]) -> DuoGlotNode:
  ''''''
  root_node = tree.get_root_node()
  assert len(root_node.get_children()) == 1, 'should not happen'
  context_node = root_node.get_children()[0]
  templatized_node = context_node.get_child_by_path(path)
  return templatized_node


def _unification_of_template_nodes_can_match_v3(
  p1_tn: DuoGlotNode,
  p2_tn: DuoGlotNode,
  to_tn: DuoGlotNode
) -> Tuple[bool, int, bool]:
  '''
  RETURN
  does unification match? what is the max match depth?
  at templatized node, do we need to change "." placeholder to "*"?
  '''
  def __rec_does_unification_match(
    p1_tn: DuoGlotNode,
    p2_tn: DuoGlotNode,
    to_tn: DuoGlotNode,
    current_depth: int
  ) -> Tuple[bool, int, bool]:
    '''
    Does the unification of p1_tn and p2_tn match to_tn?

    NOTE this is a very crude implementation.
    might miss some corner cases.

    RETURN
    does unification match?
    max depth at which match occurs
    do we need to change the dot matcher to star matcher?
    '''

    # T-NT-?
    # NT-T-?
    if p1_tn.is_terminal() and p2_tn.is_nonterminal():
      return False, current_depth, False
    if p1_tn.is_nonterminal() and p2_tn.is_terminal():
      return False, current_depth, False

    # T-T-?
    if p1_tn.is_terminal() and p2_tn.is_terminal():

      # T-T-NT
      if to_tn.is_nonterminal():
        return False, current_depth, False

      # T-T-T (scope invariant)
      if p1_tn.get_type() == p2_tn.get_type():
        if p1_tn.get_type() == to_tn.get_type():
          # exact match
          return True, current_depth, False
        else:
          return False, current_depth, False

      # _val_ ph match
      return True, current_depth, False

    # NT-NT-? (scope invariant)
    assert p1_tn.is_nonterminal()
    assert p2_tn.is_nonterminal()

    # NT-NT-T
    # NOTE not sure about this
    if to_tn.is_terminal():
      return False, current_depth, False

    # NT-NT-NT (scope invariant)
    assert to_tn.is_nonterminal()

    if p1_tn.get_type() != p2_tn.get_type():
      # ./* ph match
      if to_tn.get_num_nt_siblings() == 0:
        return True, current_depth, False
      else:
        return True, current_depth, True  # need to replace "." with "*"

    # NT=NT?=NT (scope invariant)
    if p1_tn.get_type() != to_tn.get_type():
      return False, current_depth, False

    # NOTE the most interesting part starts here
    # NT=NT=NT (scope invariant - types are identical)
    assert p1_tn.get_type() == p2_tn.get_type() == to_tn.get_type()

    num_children_p1 = len(p1_tn.get_children())
    num_children_p2 = len(p2_tn.get_children())
    num_children_to = len(to_tn.get_children())

    # check all combinations for number of children between p1 and p2 nodes
    if num_children_p1 == 1 and num_children_p2 == 1:
      if num_children_to == 1:
        return __rec_does_unification_match(p1_tn.get_children()[0], p2_tn.get_children()[0], to_tn.get_children()[0], current_depth+1)
      if p1_tn.get_children()[0].get_type() == p2_tn.get_children()[0].get_type():
        return False, current_depth, False
      return True, current_depth, True  # need to replace "." with "*"

    if num_children_p1 == 1 and num_children_p2 > 1:
      return False, current_depth, False

    if num_children_p1 > 1 and num_children_p2 == 1:
      return False, current_depth, False

    assert num_children_p1 > 1 and num_children_p2 > 1

    if num_children_p1 != num_children_p2:
      return False, current_depth, False
    if num_children_p1 != num_children_to:
      return False, current_depth, False

    # numch=numch=numch (scope invariant)
    children_can_match = []
    children_max_match_depths = []
    children_should_replace = []  # . with *
    for p1_ch, p2_ch, to_ch in zip(p1_tn.get_children(), p2_tn.get_children(), to_tn.get_children()):
      child_can_match, child_max_match_depth, child_should_replace = __rec_does_unification_match(p1_ch, p2_ch, to_ch, current_depth+1)
      children_can_match.append(child_can_match)
      children_max_match_depths.append(child_max_match_depth)
      children_should_replace.append(child_should_replace)

    return all(children_can_match), max(children_max_match_depths), any(children_should_replace)

  can_match, max_match_depth, should_replace = __rec_does_unification_match(p1_tn, p2_tn, to_tn, 1)
  return can_match, max_match_depth, should_replace


def _unification_of_template_nodes_can_match_v4(
  p1_tn: DuoGlotNode,
  p2_tn: DuoGlotNode,
  to_tn: DuoGlotNode,
  is_insert_secret_fn: bool
) -> dict:
  '''
  RETURN
  Dictionary: {
    unification_matches: bool,
    max_match_depth: int,
    replace_dot_with_star: bool
  }
  '''
  def __rec_does_unification_match(
    p1_tn: DuoGlotNode,
    p2_tn: DuoGlotNode,
    to_tn: DuoGlotNode,
    current_depth: int
  ) -> dict:
    '''
    Does the unification of p1_tn and p2_tn match to_tn?

    RETURN
    Dictionary: {
      unification_matches: bool,
      max_match_depth: int,
      replace_dot_with_star: bool
    }
    '''
    MT_TEG = 'terminal_exact_grammar'  # grammar terminals such as ',', '.', '(', ')'
    MT_TES = 'terminal_exact_semantic'  # literals, identifiers
    MT_TSEC = 'terminal_exact_secret'  # secret function call
    MT_TV = 'terminal_val'
    MT_NTDS = 'nonterminal_dotstar'
    return_dict = {
      'unification_matches': None,
      'max_match_depth': None,
      'replace_dot_with_star': None,
      'match_type': None
    }

    # T-NT-?
    if p1_tn.is_terminal() and p2_tn.is_nonterminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    # NT-T-?
    if p1_tn.is_nonterminal() and p2_tn.is_terminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    # T-T-?
    if p1_tn.is_terminal() and p2_tn.is_terminal():

      # T-T-NT
      if to_tn.is_nonterminal():
        return_dict['unification_matches'] = False
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = False
        return return_dict

      # T-T-T (scope invariant)

      if p1_tn.get_type() == p2_tn.get_type():
        if p1_tn.get_type() == to_tn.get_type():
          # exact match
          return_dict['unification_matches'] = True
          return_dict['max_match_depth'] = current_depth
          return_dict['replace_dot_with_star'] = False
          if p1_tn.get_num_siblings() == 0 and p2_tn.get_num_siblings() == 0 and to_tn.get_num_siblings() == 0:
            return_dict['match_type'] = MT_TES
          else:
            return_dict['match_type'] = MT_TEG
          return return_dict
        else:
          return_dict['unification_matches'] = False
          return_dict['max_match_depth'] = current_depth
          return_dict['replace_dot_with_star'] = False
          return return_dict

      # _val_ ph match
      return_dict['unification_matches'] = True
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return_dict['match_type'] = MT_TV
      return return_dict

    # NT-NT-? (scope invariant)
    assert p1_tn.is_nonterminal()
    assert p2_tn.is_nonterminal()

    # NT-NT-T
    # NOTE not sure about this
    if to_tn.is_terminal():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    # NT-NT-NT (scope invariant)
    assert to_tn.is_nonterminal()

    if p1_tn.get_type() != p2_tn.get_type():
      # ./* ph match
      if to_tn.get_num_nt_siblings() == 0:
        return_dict['unification_matches'] = True
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = False
        return_dict['match_type'] = MT_NTDS
        return return_dict
      else:
        # need to replace "." with "*"
        return_dict['unification_matches'] = True
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = True
        return_dict['match_type'] = MT_NTDS
        return return_dict

    # NT=NT?=NT (scope invariant)
    if p1_tn.get_type() != to_tn.get_type():
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    # NOTE the most interesting part starts here
    # NT=NT=NT (scope invariant - types are identical)
    assert p1_tn.get_type() == p2_tn.get_type() == to_tn.get_type()

    num_children_p1 = len(p1_tn.get_children())
    num_children_p2 = len(p2_tn.get_children())
    num_children_to = len(to_tn.get_children())

    # NOTE at this point, all three nodes are non-terminals AND
    # their types are identical
    # check all combinations for number of children between p1 and p2 nodes
    if num_children_p1 == 1 and num_children_p2 == 1:

      # recurse down if all of three nodes have one child each
      if num_children_to == 1:
        return __rec_does_unification_match(
          p1_tn.get_children()[0],
          p2_tn.get_children()[0],
          to_tn.get_children()[0],
          current_depth + 1
        )

      if p1_tn.get_children()[0].get_type() == p2_tn.get_children()[0].get_type():
        return_dict['unification_matches'] = False
        return_dict['max_match_depth'] = current_depth
        return_dict['replace_dot_with_star'] = False
        return return_dict

      # need to replace "." with "*"
      return_dict['unification_matches'] = True
      return_dict['max_match_depth'] = current_depth + 1
      return_dict['replace_dot_with_star'] = True
      return_dict['match_type'] = MT_NTDS
      return return_dict

    if num_children_p1 == 1 and num_children_p2 > 1:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    if num_children_p1 > 1 and num_children_p2 == 1:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    assert num_children_p1 > 1 and num_children_p2 > 1

    if num_children_p1 != num_children_p2:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    if num_children_p1 != num_children_to:
      return_dict['unification_matches'] = False
      return_dict['max_match_depth'] = current_depth
      return_dict['replace_dot_with_star'] = False
      return return_dict

    # numch=numch=numch (scope invariant)
    children_can_match = []
    children_max_match_depths = []
    children_should_replace = []  # . with *
    children_match_types = []
    for p1_ch, p2_ch, to_ch in zip(p1_tn.get_children(), p2_tn.get_children(), to_tn.get_children()):
      result_dict = __rec_does_unification_match(p1_ch, p2_ch, to_ch, current_depth+1)
      children_can_match.append(result_dict['unification_matches'])
      children_max_match_depths.append(result_dict['max_match_depth'])
      children_should_replace.append(result_dict['replace_dot_with_star'])
      children_match_types.append(result_dict['match_type'])

    return_dict['unification_matches'] = all(children_can_match)
    return_dict['max_match_depth'] = max(children_max_match_depths)
    return_dict['replace_dot_with_star'] = children_should_replace
    return_dict['match_type'] = children_match_types
    return return_dict

  SECRET_FN = 'secret_fun_4071'
  if is_insert_secret_fn:
    p1_tokens = p1_tn.get_terminal_tokens()
    p2_tokens = p2_tn.get_terminal_tokens()
    if SECRET_FN in p1_tokens and SECRET_FN in p2_tokens:
      # both should be only secret function invocation
      if len(p1_tokens) > 1 or len(p2_tokens) > 1:
        return {
          'unification_matches': False,
          'max_match_depth': 3,
          'replace_dot_with_star': False,
          'match_type': None
        }
      if p1_tokens[0] == p2_tokens[0] == SECRET_FN:
        return {
          'unification_matches': True,
          'max_match_depth': 1,
          'replace_dot_with_star': False,
          'match_type': 'terminal_exact_secret'
        }
      return {
        'unification_matches': False,
        'max_match_depth': 3,
        'replace_dot_with_star': False,
        'match_type': None
      }

  result_dict = __rec_does_unification_match(p1_tn, p2_tn, to_tn, 1)
  return result_dict


def _is_generated_code_type_isomorphic_to_shallow_template_v3(
  gen_tree: DuoGlotTree,
  template_tree: DuoGlotTree,
  templatized_node_paths: List[List[int]]
) -> bool:
  '''
  everything except templatized nodes (holes) is the same
  templatized nodes can be arbitrarily different
  NOTE refer to notes or update this doc
  '''

  gen_type_enc = _get_tree_encoding_except_templatized_nodes_v3(gen_tree, templatized_node_paths)
  if gen_type_enc is None:
    return False
  template_type_enc = _get_tree_encoding_except_templatized_nodes_v3(template_tree, templatized_node_paths)
  assert template_type_enc is not None, 'should not happen: templatized_node_ids are invalid'

  return gen_type_enc == template_type_enc


def _get_tree_encoding_except_templatized_nodes_v3(
  tree: DuoGlotTree,
  templatized_node_paths: List[List[int]]
) -> Union[str, None]:
  '''
  Get string encoding of a tree
  Return None if any of templatized nodes is missing from tree
  TODO update this doc
  '''
  def _rec_post_order(node: DuoGlotNode):
    nonlocal templatized_nodes
    if node in templatized_nodes:
      return '__'
    if isinstance(node, TNode):
      return node.get_type()
    children_encoding = ''
    for child in node.get_children():
      children_encoding += _rec_post_order(child)
    return f'{node.get_type()} ({children_encoding})'

  root_node = tree.get_root_node()

  # get_child_by_path() relative to context node
  # context node should be the only child when its text is parsed as it is
  # refer to s_templatizer.._rec_collect_templatized_node_ids
  # TODO this may need refactoring
  if len(root_node.get_children()) != 1:
    return None

  context_node = root_node.get_children()[0]
  templatized_nodes = [context_node.get_child_by_path(path) for path in templatized_node_paths]

  if any(map(lambda node: node is None, templatized_nodes)):
    return None

  return _rec_post_order(tree.get_root_node())


def _get_tree_serialize_as_str(program: str) -> str:
  '''
  Given a source of a program,
  1. Get a tree from it and
  2. Serialize the tree as string

  PRE: `program` does not have parse errors
  POST: semantically equivalent programs will have the same serialization
  '''
  # TODO hard-coded to Python
  program_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, program, 'py')
  program_tree = DuoGlotTree(program_ast)
  return _serialize_as_str(program_tree)
def _serialize_as_str(tree: DuoGlotTree) -> str:


  '''
  Get a tree representation of DuoGlot tree.
  POST: serialize(tree1) == serizalize(tree2) ==> tree1 == tree2
  '''
  def _rec_post_order(node: DuoGlotNode):
    if isinstance(node, TNode):
      return node.get_type()
    children_encoding = ''
    for child in node.get_children():
      children_encoding += _rec_post_order(child)
    return f'({node.get_type()} {children_encoding})'

  return _rec_post_order(tree.get_root_node())


def _check_templatized_nodes_depths(
  gen_tree: DuoGlotTree,
  templatized_node_paths: List[List[int]],
  max_depth=2
) -> bool:
  ''''''
  root_node = gen_tree.get_root_node()
  # get_child_by_path() relative to context node
  # context node should be the only child when its text is parsed as it is
  # refer to s_templatizer.._rec_collect_templatized_node_ids
  # TODO this may need refactoring
  if len(root_node.get_children()) != 1:
    return False
  context_node = root_node.get_children()[0]
  templatized_nodes = [context_node.get_child_by_path(path) for path in templatized_node_paths]
  if any(map(lambda node: node is None, templatized_nodes)):
    return False
  for node in templatized_nodes:
    if node.get_depth() > max_depth:
      return False
  return True


def _templatized_nodes_have_different_tokens(
  program1: str,
  program2: str,
  templatized_node_paths: List[List[int]]
) -> bool:
  '''
  given two programs, check if templatized nodes have different tokens or not
  PRE: max depth at templatized nodes is 2
  '''
  program_trees : List[DuoGlotTree] = []
  for program in [program1, program2]:
    program_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, program, 'py')
    program_tree = DuoGlotTree(program_ast)
    program_trees.append(program_tree)

  tokens_at_templatized_nodes = []
  for templatized_node_path in templatized_node_paths:
    for program_tree in program_trees:
      root_node = program_tree.get_root_node()
      assert len(root_node.get_children()) == 1, 'should not happen'
      context_node = root_node.get_children()[0]
      templatized_node = context_node.get_child_by_path(templatized_node_path)
      tokens_at_of = program_tree.get_terminal_tokens_at_node(templatized_node)
      assert len(tokens_at_of) == 1, 'max depth is 2 implies NT nodes with single T child'
      tokens_at_templatized_nodes.extend(tokens_at_of)

  if len(tokens_at_templatized_nodes) != len(set(tokens_at_templatized_nodes)):
    return False
  return True


def _calculate_match_penalty(templatized_node_match_types: list) -> float:
  ''''''
  dict_counts = {}
  def __rec_count_types(tnmt: Union[list, str, None]):
    nonlocal dict_counts
    if isinstance(tnmt, str) or tnmt is None:
      dict_counts[tnmt] = dict_counts.get(tnmt, 0) + 1
      return
    assert isinstance(tnmt, list), str(type(tnmt))
    for elem in tnmt:
      __rec_count_types(elem)
  __rec_count_types(templatized_node_match_types)
  MT_TEG = 'terminal_exact_grammar'  # nothing
  MT_TES = 'terminal_exact_semantic'  # bad -> repeating tokens
  MT_TSEC = 'terminal_exact_secret'  # very good
  MT_TV = 'terminal_val'  # good -> simpler programs
  MT_NTDS = 'nonterminal_dotstar'  # bad -> more complex programs
  MT_NULL = None  # very bad -> no match
  match_penalty = 1
  match_penalty *= math.pow(1, dict_counts.get(MT_TEG, 0))
  match_penalty *= math.pow(3, dict_counts.get(MT_TES, 0))
  match_penalty *= math.pow(10, -dict_counts.get(MT_TSEC, 0))
  match_penalty *= math.pow(2, -dict_counts.get(MT_TV, 0))
  match_penalty *= math.pow(2, dict_counts.get(MT_NTDS, 0))
  match_penalty *= math.pow(10, dict_counts.get(MT_NULL, 0))
  return match_penalty


def _tree_edit_distance(program1_tree: DuoGlotTree, program2_tree: DuoGlotTree) -> float:
  ''''''
  pr1 = program1_tree.tree_as_list()
  pr2 = program2_tree.tree_as_list()
  dist = ast_match.distance_of_AST_frags(pr1, pr2, None)
  return dist


# old implementation
def _is_generated_code_type_isomorphic_to_template_origin(gen_tree: DuoGlotTree, template_tree: DuoGlotTree) -> bool:
  '''
  Return False if AST's do not match, True if AST's match.

  What is an AST match?
  AST's match iff they are isomorphic AND the types of corresponding non-terminal nodes are identical.
  Refer to: https://www.baeldung.com/cs/isomorphic-trees

  PARAMS
  generated_ast - DuoGlot-style AST of generated code
  template_origin_ast - DuoGlot-style AST of template origin code

  RETURN
  return_dict = {
    type_isomorphic: bool
  }

  TODO are these isomorphic?
  'def f_gold(gpa: float) -> int:\n    some_secret_fn_4071()',
  'def f_gold(zzzzz: ZZZZZ) -> float:\n    some_secret_fn_4071()',
  '''

  gen_type_ahu_enc = _get_type_ahu_encoding(gen_tree)
  template_type_ahu_enc = _get_type_ahu_encoding(template_tree)

  type_isomorphic = gen_type_ahu_enc == template_type_ahu_enc

  return type_isomorphic


def _get_type_ahu_encoding(tree: DuoGlotTree) -> str:
  '''
  Compute AHU encoding with type information for comparing tree for type-isomorphism
  https://www.baeldung.com/cs/isomorphic-trees#1-ahu-encoding
  '''
  def _rec_post_order(node: DuoGlotNode):
    if isinstance(node, TNode):
      return '0'
    children_encoding = ''
    for child in node.get_children():
      children_encoding += _rec_post_order(child)
    return f'({node.get_type()} {children_encoding})'

  return _rec_post_order(tree.get_root_node())


# not used, for reference
def _get_ahu_encoding(tree: DuoGlotTree) -> str:
  '''
  Compute AHU encoding for comparing tree for isomorphism
  https://www.baeldung.com/cs/isomorphic-trees#1-ahu-encoding
  '''
  def _rec_post_order(node: DuoGlotNode):
    if isinstance(node, TNode):
      return '0'
    children_encoding = ''
    for child in node.get_children():
      children_encoding += _rec_post_order(child)
    return f'({children_encoding})'

  return _rec_post_order(tree.get_root_node())

# ==============================================================================
# ================= POST-PROCESSING TRANSLATED CODE (SP1) ======================
# ==============================================================================

def post_process_program_pairs(
  data_to_postprocess: dict
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

  return_dict = {}
  return_dict['good_program_pairs'] = []
  return_dict['success'] = False

  program_pairs : list = data_to_postprocess['program_pairs']
  contexts : dict = data_to_postprocess['contexts']

  good_program_pairs = []
  for program_pair in program_pairs:
    if _program_pair_satisfies_criteria(program_pair, contexts):
      good_program_pairs.append(program_pair)

  if len(good_program_pairs) == 0:
    return return_dict

  return_dict['success'] = True
  return_dict['good_program_pairs'] = good_program_pairs
  return return_dict


def _program_pair_satisfies_criteria(
  program_pair: dict,
  contexts: dict
) -> bool:
  ''''''
  source_program = program_pair['source']
  target_program = program_pair['target']

  # criteria 1
  if has_parse_error(target_program, lang='js'):
    return False

  # criteria 2
  source_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, source_program, 'py')
  source_tree = DuoGlotTree(source_ast)
  target_ast, _ = ast_parse.parse_text_dbg(JS_LANGUAGE, target_program, 'js')
  target_tree = DuoGlotTree(target_ast)

  all_contained_contexts = _get_all_contexts_contained(
    [source_tree],
    [target_tree],
    contexts
  )

  if len(all_contained_contexts) > 0:
    return True

  return False


# ==============================================================================
# ================= POST-PROCESSING TRANSLATED CODE (SP2) ======================
# ==============================================================================

def post_process_translation_pair(
  data_to_postprocess: dict
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

  return_dict = {}
  return_dict['translation_pairs'] = []
  return_dict['success'] = False

  sp1 : str = data_to_postprocess['sp1']
  sp2 : str = data_to_postprocess['sp2']
  cand_translation_sp1 : str = data_to_postprocess['cand_translation_sp1']
  raw_translations_sp2 : list = data_to_postprocess['raw_translations_sp2']
  contexts : dict = data_to_postprocess['contexts']

  for raw_translation_sp2 in raw_translations_sp2:
    sp2_translation_is_good = _raw_translation_sp2_satisfies_criteria(
      sp1,
      sp2,
      cand_translation_sp1,
      raw_translation_sp2,
      contexts
    )
    if sp2_translation_is_good:
      return_dict['translation_pairs'].append([
        {'source': sp1, 'target': cand_translation_sp1},
        {'source': sp2, 'target': raw_translation_sp2},
      ])

  if len(return_dict['translation_pairs']) > 0:
    return_dict['success'] = True

  return return_dict


def _raw_translation_sp2_satisfies_criteria(
  sp1: str,
  sp2: str,
  cand_translation_sp1: str,
  raw_translation_sp2: str,
  contexts: dict
) -> bool:
  ''''''

  # criteria 1
  if has_parse_error(raw_translation_sp2, lang='js'):
    return False

  # criteria 2
  are_targets_type_isomorphic = _are_translations_identical_except_identifiers(
    cand_translation_sp1,
    raw_translation_sp2
  )
  if not are_targets_type_isomorphic:
    return False

  # criteria 3
  source_trees : List[DuoGlotTree] = []
  for source in [sp1, sp2]:
    source_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, source, 'py')
    source_tree = DuoGlotTree(source_ast)
    source_trees.append(source_tree)
  target_trees : List[DuoGlotTree] = []
  for target in [cand_translation_sp1, raw_translation_sp2]:
    target_ast, _ = ast_parse.parse_text_dbg(JS_LANGUAGE, target, 'js')
    target_tree = DuoGlotTree(target_ast)
    target_trees.append(target_tree)

  contexts_contained = _get_all_contexts_contained(source_trees, target_trees, contexts)
  if len(contexts_contained) == 0:
    return False

  return True


def get_translation_pairs_from_program_pairs(data_to_postprocess: dict):
  '''
  Given a list of program pairs, make valid translation pair combinations from them.

  CRITERIA
  1. Programs should not have translation pairs
  2. The source programs are identical to the template everywhere except
  templatized nodes. It means that we are checking the templatized nodes.




  1. Sources should have different tokens at corresponding placeholders/holes
  2. Targets should be (i) parseable w/o errors, (ii) type-isomorphic, additionally terminal isomorphic except identifiers (compatible) between each other
  3. Contexts should be available in source and target code (at least one context)

  pairs: [{
    source: source_prog,  // program generated from template
    target: target_prog   // translated program
  }, ...]

  TERMS
  program pair - a single program in src language ant its translation in tar language
  translation pair - a pair of 'program pairs', used as an input to rule inference.

  RETURN
  return_dict = {
    translation_pairs_stats: List,
    translation_pairs: List,
    success: bool,
  }
  '''

  # get the data sent from frontend
  program_pairs = data_to_postprocess['program_pairs']
  template = data_to_postprocess['template']
  template_origin = data_to_postprocess['template_origin']
  templatized_node_ids = data_to_postprocess['templatized_node_ids']
  contexts = data_to_postprocess['contexts']

  assert len(contexts) > 0, 'sanity check: there is at least one context per translation pair'

  # TODO pre-fill this dict
  return_dict = {}
  return_dict['translation_pairs_stats'] = []

  # 1 iterate over ALL POSSIBLE program pair combinations
  for i in range(len(program_pairs)):
    for j in range(i + 1, len(program_pairs)):
      candidate_translation_pair = [program_pairs[i], program_pairs[j]]
      candidate_translation_pair_stats = _post_process_translation_pair(
        candidate_translation_pair,
        template_origin,
        templatized_node_ids,
        contexts
      )
      return_dict['translation_pairs_stats'].append(candidate_translation_pair_stats)

  # 2 select all translation pairs that satisfy our criteria
  translation_pairs = []
  for candidate_translation_pair_stats in return_dict['translation_pairs_stats']:
    if candidate_translation_pair_stats['success']:
      translation_pairs.append(candidate_translation_pair_stats['translation_pair'])
  return_dict['translation_pairs'] = translation_pairs
  return_dict['success'] = len(translation_pairs) > 0

  return return_dict


def _post_process_translation_pair(
  translation_pair,
  template_origin,
  templatized_node_ids,
  contexts
):
  '''
  Given a translation pair (two program pairs that are input to the rule inference),
  tell whether this translation is possible or not

  translation pair: [
    {source: source_program1, target: target_program2},
    {source: source_program2, target: target_program2},
  ]

  PRE1: both source programs are type-isomorphic to template

  CRITERIA:
  Documented in caller function

  RETURN:
  return_dict = {
    translation_pair: <>
    success: bool,
    reasons: List[str],
    sources_have_repeating_tokens: bool,
    targets_are_compatible: bool,
    context_exists: bool,
  }

  TODO NOTE hard-coded to Python-JavaScript
  '''

  # TODO pre-fill return dict
  return_dict = {}
  return_dict['translation_pair'] = translation_pair
  return_dict['success'] = False
  return_dict['reasons'] = []

  source1 = translation_pair[0]['source']
  target1 = translation_pair[0]['target']
  source2 = translation_pair[1]['source']
  target2 = translation_pair[1]['target']

  # sanity check
  if has_parse_error(source1, lang='py'):
    return_dict['reasons'].append('source1 has parse error')
    return return_dict
  if has_parse_error(source2, lang='py'):
    return_dict['reasons'].append('source2 has parse error')
    return return_dict
  if has_parse_error(target1, lang='js'):
    return_dict['reasons'].append('target1 has parse error')
    return return_dict
  if has_parse_error(target2, lang='js'):
    return_dict['reasons'].append('target2 has parse error')
    return return_dict

  # 1 get trees of source programs
  source_trees : List[DuoGlotTree] = []
  for source in [source1, source2]:
    source_ast, _ = ast_parse.parse_text_dbg(PY_LANGUAGE, source, 'py')
    source_tree = DuoGlotTree(source_ast)
    source_trees.append(source_tree)
  target_trees : List[DuoGlotTree] = []
  for target in [target1, target2]:
    target_ast, _ = ast_parse.parse_text_dbg(JS_LANGUAGE, target, 'js')
    target_tree = DuoGlotTree(target_ast)
    target_trees.append(target_tree)

  # 2 check tokens at corresponding templatized nodes (criteria 1)
  return_dict['sources_have_repeating_tokens'] = False

  for templatized_node_id in templatized_node_ids:
    tokens_at_templatized_nodes = []
    for source_tree in source_trees:
      root_node = source_tree.get_root_node()
      assert len(root_node.get_children()) == 1, 'should not happen'
      context_node = root_node.get_children()[0]
      templatized_node = context_node.get_child_by_path(templatized_node_ids[templatized_node_id])
      tokens_at_of = source_tree.get_terminal_tokens_at_node(templatized_node)

      if len(tokens_at_of) > 1:
        return_dict['reasons'].append('multiple tokens at templatized node')

      tokens_at_templatized_nodes.extend(tokens_at_of)

    if len(tokens_at_templatized_nodes) != len(set(tokens_at_templatized_nodes)):
      return_dict['sources_have_repeating_tokens'] = True
      return_dict['reasons'].append('source have repeating tokens at corresponding templatized nodes')
      break

  # 3 check targets for compatibility
  are_targets_compatible = _are_translations_identical_except_identifiers(target1, target2)
  return_dict['targets_are_compatible'] = are_targets_compatible
  if not are_targets_compatible:
    return_dict['reasons'].append('targets are not compatible')

  # 4 contexts
  return_dict['contexts_contained'] = _get_all_contexts_contained(source_trees, target_trees, contexts)
  return_dict['at_least_one_context_exists'] = len(return_dict['contexts_contained']) > 0
  if not return_dict['at_least_one_context_exists']:
    return_dict['reasons'].append('none of the contexts exists for source or target')

  return_dict['success'] = len(return_dict['reasons']) == 0
  return return_dict


def _are_translations_identical_except_identifiers(trans1: str, trans2: str):
  '''
  Two translations (programs in the target language) are identical iff
  1. The trees are type isomorphic (refer to `is_generated_code_type_isomorphic_to_template_origin`)
  2. All terminals EXCEPT identifiers are identical

  PRE1: trans1 does not have parse errors
  PRE2: trans2 does not have parse errors

  TODO hard-coded to JavaScript
  '''

  trans1_ast, _ = ast_parse.parse_text_dbg(JS_LANGUAGE, trans1, 'js')
  trans2_ast, _ = ast_parse.parse_text_dbg(JS_LANGUAGE, trans2, 'js')
  trans1_tree = DuoGlotTree(trans1_ast)
  trans2_tree = DuoGlotTree(trans2_ast)

  trans1_enc = _get_type_ahu_ter_x_ident_encoding(trans1_tree)
  trans2_enc = _get_type_ahu_ter_x_ident_encoding(trans2_tree)

  are_compatible = trans1_enc == trans2_enc

  return are_compatible


def _get_type_ahu_ter_x_ident_encoding(tree: DuoGlotTree) -> str:
  '''
  Compute AHU encoding with
  1. type information
  2. terminals except identifiers
  3. terminals except literals
  for comparing tree for type-isomorphism
  https://www.baeldung.com/cs/isomorphic-trees#1-ahu-encoding

  TODO this is hard-coded to JavaScript
  '''

  def _rec_post_order(node: DuoGlotNode):
    if isinstance(node, TNode):
      # if node.get_parent().get_type() in _JS_IDENTIFIER_LITERAL_TYPES:
      #   return '0'
      return node.get_type()

    if node.is_terminal():
      if node.get_num_siblings() == 0:
        return '0'
    if node.has_single_terminal_child():
      return '0'

    children_encoding = ''
    for child in node.get_children():
      children_encoding += _rec_post_order(child)
    return f'({node.get_type()} {children_encoding})'

  return _rec_post_order(tree.get_root_node())


def _unify_trees(trees: List[DuoGlotTree]):
  '''
  Unify two trees for checking target programs of translation pairs
  TODO update later
  '''

  def __rec(nodes: List[DuoGlotNode]):
    '''
    PRE: node types of nodes are identical
    PRE: all nodes are terminals or nonterminals
    '''

    # sanity check
    all_terminals = all([node.is_terminal() for node in nodes])
    all_nonterminals = all([node.is_nonterminal() for node in nodes])
    assert all_terminals or all_nonterminals

    # sanity check
    have_same_node_types = all([node.get_type() == nodes[0].get_type() for node in nodes])
    assert have_same_node_types

    if nodes[0].is_terminal():
      return [nodes[0].get_type()]

    common_root = [nodes[0].get_type()]

    # make a hole if number of children is different
    have_same_num_children = all([len(node.get_children()) == len(nodes[0].get_children()) for node in nodes])
    if not have_same_num_children:
      common_root.append(['HOLE_DIFF_NUM_CHILDREN'])
      return common_root

    common_children = []
    nodes_children = [node.get_children() for node in nodes]
    for i in range(len(nodes[0].get_children())):
      ith_children = [node_children[i] for node_children in nodes_children]

      all_children_terminals = all([ith_child.is_terminal() for ith_child in ith_children])
      all_children_nonterminals = all([ith_child.is_nonterminal() for ith_child in ith_children])
      if not all_children_terminals and not all_children_nonterminals:
        common_children.append('HOLE_NT_T_NODE')
        continue

      children_have_same_node_types = all([node.get_type() == ith_children[0].get_type() for node in ith_children])

      if all_children_terminals:
        if children_have_same_node_types:
          common_children.extend(__rec(ith_children))
        else:
          common_children.append('HOLE_DIFF_T')
        continue

      if all_children_nonterminals:
        if children_have_same_node_types:
          common_children.extend(__rec(ith_children))
        else:
          common_children.append('HOLE_DIFF_NT')
        continue

      raise RuntimeError('should not happen')

    common_root.append(common_children)
    return common_root

  root_nodes = [tree.get_root_node() for tree in trees]
  unified_tree = __rec(root_nodes)
  return unified_tree


def _get_all_contexts_contained(
  source_trees: List[DuoGlotTree],
  target_trees: List[DuoGlotTree],
  contexts: list,
):
  ''''''
  contexts_contained = []
  for context in contexts:
    if _context_exists(source_trees, target_trees, context['source_context'], context['target_context']):
      contexts_contained.append(context)
  return contexts_contained


def _context_exists(
  src_trees: List[DuoGlotTree],
  tar_trees: List[DuoGlotTree],
  src_ctx: list,
  tar_ctx: list,
) -> bool:
  '''
  Implementation of this function is similar to s_post_process_translation_rule.TranslationRule.trim_context()
  '''

  def __are_previous_siblings(node: DuoGlotNode, sibling_types: List[str]) -> bool:
    '''
    PRE: siblings are ordered naturally (as appeared in tree)

    IDEA
    Get all NT siblings to the left, make 1-1 comparison
    '''
    assert isinstance(node, DuoGlotNode)
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

  def __are_parents(node: DuoGlotNode, parent_types: List[str]) -> bool:
    '''
    PRE: siblings are ordered naturally (as appeared in tree)

    IDEA
    Starting from immediate parent, go up until reach root node OR
    exhaust parent_types, make 1-1 comparison
    '''
    assert isinstance(node, DuoGlotNode)

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
    node: DuoGlotNode,
    sibling_types: List[str],
    parent_types: List[str]
  ) -> Union[DuoGlotNode, None]:
    '''
    Return the earliest occurence of the node
    '''
    if isinstance(node, TNode):
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

  def __get_node_under_context(root_node: DuoGlotNode, siblings: list, parents: list) -> DuoGlotNode:
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


# for testing
def _test_get_translation_pairs_from_program_pairs():

  program_pairs = [
    {
      "source": "midVal1 = 5 if x + y - 1 < m else 10",
      "target": "let midVal1 = (x + y - 1 < m) ? 5 : 10;"
    },
    {
      "source": "midVal1 = 5 if 3 + 2 - 1 < m else 10",
      "target": "let midVal1 = (3 + 2 - 1 < m) ? 5 : 10;"
    },
    {
      "source": "midVal1 = 5 if (2*2) + (3/3) - 1 < m else 10",
      "target": "let midVal1 = ((2 * 2) + (3 / 3) - 1 < m) ? 5 : 10;"
    },
    {
      "source": "midVal1 = 5 if (2*2) + (3/3) - 1 < m else 10",
      "target": "var midVal1;\nif ((2 * 2) + (3 / 3) - 1 < m) {\n    midVal1 = 5;\n} else {\n    midVal1 = 10;\n}"
    },
    {
      "source": "midVal1 = 5 if 2 + 3 - 1 < m else 10",
      "target": "let midVal1 = (2 + 3 - 1 < m) ? 5 : 10;"
    },
    {
      "source": "midVal1 = 5 if (2*2) + (3*3) - 1 < m else 10",
      "target": "let m;\nlet midVal1 = ((2*2) + (3*3) - 1 < m) ? 5 : 10;"
    }
  ]

  program_pairs = [
    {
      "source": "midVal1 = 5 if x + y - 1 < m else 10",
      "target": "let midVal1 = x + y - 1 < m ? 5 : 10;"
    },
    {
      "source": "midVal1 = 5 if 3 + 2 - 1 < m else 10",
      "target": "let midVal1 = 3 + 2 - 1 < m ? 5 : 10;"
    }
  ]


  template = 'midVal1 = 5 if __ + __ - 1 < m else 10'
  template_origin = 'midVal1 = 5 if i + k // 2 - 1 < m else 10'
  templatized_node_ids = {
    "17": [
      0,
      2,
      2,
      0,
      0,
      0
    ],
    "18": [
      0,
      2,
      2,
      0,
      0,
      2
    ]
  }
  contexts = [
    {
      "source_context": {
        "siblings": [],
        "parents": [
          "\"py.binary_operator\"",
          "\"py.comparison_operator\"",
          "\"py.conditional_expression\"",
          "\"py.assignment\"",
          "\"py.expression_statement\""
        ]
      },
      "target_context": {
        "siblings": [],
        "parents": [
          "\"js.binary_expression\"",
          "\"js.binary_expression\"",
          "\"js.ternary_expression\"",
          "\"js.variable_declarator\"",
          "\"js.lexical_declaration\""
        ]
      }
    }
  ]

  data_to_post_process = {
    'program_pairs': program_pairs,
    'template': template,
    'template_origin': template_origin,
    'templatized_node_ids': templatized_node_ids,
    'contexts': contexts
  }

  result_dict = get_translation_pairs_from_program_pairs(data_to_post_process)
  with open('temporary_test_get_translation_pairs_from_program_pairs.json', 'w') as fout:
    fout.write(json.dumps(result_dict))
  # print(result_dict)


def _test_post_process_generated_code_blocks_v3():
  lang = 'py'
  template_origin = "for i, v in enumerate(nums):\n    num = target - v\n    if num in helper:\n        return [helper[num], i]\n    helper[v] = i"
  template = "for __ in enumerate(__):\n    __"
  templatized_node_ids =  {
    "2": [
      1
    ],
    "8": [
      3,
      1,
      1
    ],
    "9": [
      5
    ]
  }
  generated_code_blocks1 = [
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for i, val in enumerate([1, 2, 3, 4]):\n    secret_fun_4071()",
    "for i, val in enumerate(['apple', 'banana', 'cherry']):\n    secret_fun_4071()",
    "for i, val in enumerate([{'name': 'apple'}, {'name': 'banana'}, {'name': 'cherry'}]):\n    secret_fun_4071()",
    "for i, item in enumerate(nums):\n    secret_fun_4071()",
    "for index, value in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for count, element in enumerate(my_list):\n    secret_fun_4071()",
    "for position, data in enumerate(dataset):\n    secret_fun_4071()",
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for i, val in enumerate([\"apple\", \"banana\", \"cherry\"]):\n    secret_fun_4071()",
    "for i, val in enumerate(nums):\n    secret_fun_4071()",
    "for index, item in enumerate(my_list):\n    secret_fun_4071()",
    "for key, value in enumerate(dictionary):\n    secret_fun_4071()",
    "for char_index, char in enumerate(string):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    secret_fun_4071()",
    "for 0 in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for x in enumerate(y for y in range(10)):\n    secret_fun_4071()",
    "for _ in enumerate([secret_fun_4071() for _ in range(10)]):\n    break",
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for index, value in enumerate(numbers):\n    secret_fun_4071()",
    "for idx, item in enumerate(items):\n    secret_fun_4071()",
    "for count, element in enumerate(elements):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    secret_fun_4071()",
    "for index, value in enumerate(array):\n    secret_fun_4071()",
    "for count, element in enumerate(elements):\n    secret_fun_4071()",
    "for index, val in enumerate(my_list):\n    secret_fun_4071()",
    "for 1 in enumerate([1,2,3]):\n    secret_fun_4071()",
    "for _ in enumerate(['a', 'b', 'c']):\n    secret_fun_4071()",
    "for key, value in enumerate({'a':1, 'b':2}.items()):\n    secret_fun_4071()",
    "for index, value in enumerate(my_list):\n    secret_fun_4071()",
    "for 0, \"item\" in enumerate(\"hello\"):\n    secret_fun_4071()",
    "for index, value in enumerate([1, 2, 3, 4]):\n    secret_fun_4071()",
    "for index, value in enumerate({\"a\": 1, \"b\": 2}):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    secret_fun_4071()",
    "for 0 in enumerate([1, 2, 3]):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    print(item)",
    "for i, item in enumerate(my_list):\n    if item == \"target\":\n        break",
    "for idx, val in enumerate(my_list):\n    secret_fun_4071()",
    "for x, y in enumerate(numbers):\n    secret_fun_4071()",
    "for i, num in enumerate(data):\n    secret_fun_4071()",
    "for idx, element in enumerate(my_list):\n    secret_fun_4071()",
    "for i, _ in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for k, v in enumerate({'a':1, 'b':2}.items()):\n    secret_fun_4071()",
    "for i, item in enumerate([{'name':'John', 'age':25}, {'name':'Jane', 'age':30}]):\n    secret_fun_4071()",
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for index, value in enumerate(data):\n    secret_fun_4071()",
    "for num, item in enumerate(collection):\n    secret_fun_4071()",
    "for count, element in enumerate(elements):\n    secret_fun_4071()",
    "for index, item in enumerate(my_list):\n    secret_fun_4071()",
    "for 0, 'a' in enumerate('hello'):\n    secret_fun_4071()",
    "for _ in enumerate(range(10)):\n    secret_fun_4071()",
    "for i, value in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for i, val in enumerate(nums):\n    secret_fun_4071()",
    "for 0, 'a' in enumerate('hello'):\n    secret_fun_4071()",
    "for i, val in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for i, val in enumerate({\"apple\": 1, \"banana\": 2}):\n    secret_fun_4071()"
  ]
  generated_code_blocks2 = [
    "for i, item in enumerate(items):\n    secret_fun_4071()",
    "for idx, value in enumerate(my_list):\n    secret_fun_4071()",
    "for index, element in enumerate(data):\n    secret_fun_4071()",
    "for count, word in enumerate(words):\n    secret_fun_4071()",
    "for i, val in enumerate(items):\n    secret_fun_4071()",
    "for 1, 2 in enumerate([3, 4, 5]):\n    secret_fun_4071()",
    "for _ in enumerate(__):\n    secret_fun_4071()",
    "for i, val in enumerate(['apple', 'banana', 'cherry']):\n    secret_fun_4071()",
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for 0, 1 in enumerate([1, 2, 3, 4, 5]):\n    secret_fun_4071()",
    "for idx, item in enumerate(['a', 'b', 'c']):\n    secret_fun_4071()",
    "for index, element in enumerate({\"key1\": \"value1\", \"key2\": \"value2\"}):\n    secret_fun_4071()",
    "for i, val in enumerate(my_list):\n    secret_fun_4071()",
    "for 0, 'a' in enumerate('hello'):\n    secret_fun_4071()",
    "for item in enumerate(data):\n    secret_fun_4071()",
    "for index, value in enumerate(numbers):\n    secret_fun_4071()",
    "for idx, item in enumerate(my_list):\n    secret_fun_4071()",
    "for 1, 'a' in enumerate('string'):\n    secret_fun_4071()",
    "for _, _ in enumerate(_):\n    secret_fun_4071()",
    "for idx, (sub_idx, sub_item) in enumerate([(1, 'a'), (2, 'b')]):\n    secret_fun_4071()",
    "for index, item in enumerate(numbers):\n    secret_fun_4071()",
    "for i, value in enumerate(list1):\n    secret_fun_4071()",
    "for idx, element in enumerate(array):\n    secret_fun_4071()",
    "for count, data in enumerate(dataset):\n    secret_fun_4071()",
    "for num, entry in enumerate(entries):\n    secret_fun_4071()",
    "for i, item in enumerate(lst):\n    secret_fun_4071()",
    "for index, element in enumerate(array):\n    secret_fun_4071()",
    "for count, value in enumerate(numbers):\n    secret_fun_4071()",
    "for position, data in enumerate(sequence):\n    secret_fun_4071()",
    "for index, value in enumerate(my_list):\n    secret_fun_4071()",
    "for i, item in enumerate(data):\n    secret_fun_4071()",
    "for i, element in enumerate(elements):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    secret_fun_4071()",
    "for 1, 'a' in enumerate('string'):\n    secret_fun_4071()",
    "for i, item in enumerate(my_list):\n    if i == 0:\n        break\n    elif i == 1:\n        continue\n    else:\n        return i",
    "for i, item in enumerate(my_list):\n    print(i)"
  ]
  generated_code_blocks = generated_code_blocks1

  data2pp = {
    'lang': lang,
    'template_origin': template_origin,
    'templatized_node_ids': templatized_node_ids,
    'generated_code_blocks': generated_code_blocks,
    'is_insert_secret_fn': True
  }

  pp_result = post_process_generated_code_blocks_v3(data2pp)

  with open('temporary_test_post_post_process_generated_code_blocks_v3.json', 'w') as fout:
    fout.write(json.dumps(pp_result))


def _test_post_process_translation_pair():
  data2pp = {
    "sp1": "if condition:\n    secret_fun_4071()",
    "sp2": "if 5 > 3:\n    secret_fun_4071()",
    "cand_translation_sp1": "if (condition) {\n    secret_fun_4071();\n}",
    "raw_translations_sp2": [
      "if (5 > 3) {\n    secret_fun_4071();\n}"
    ],
    "contexts": [
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      },
      {
        "source_context": {
          "siblings": [],
          "parents": []
        },
        "target_context": {
          "siblings": [],
          "parents": []
        }
      }
    ]
  }
  pp_result = post_process_translation_pair(data2pp)
  with open('temporary_test_post_process_translation_pair.json', 'w') as fout:
    fout.write(json.dumps(pp_result))


def _test_unify_trees():
  jss = {
    'all': [
      'let x = 5;',
      'let y = "hello";',
      'let y = foo(1, 2, 3);',
      'let y = 10 + 5;',
      'let [name, age] = ["bob", 11];',
      'let z = a = b;',
    ],
    '1': [
      'let x = 5;',
      'var x = 5;',
    ],
    '2': [
      'let x = 5;',
      'const x = 5;',
    ],
    '3': [
      'var x = 5;',
      'const x = 5;',
    ],
    '4': [
      'let x = 5;',
      'x = 5;'
    ],
    '5': [
      'let x = 5;',
      'let y = "hello";',
    ],
    '6': [
      'let x = 5;',
      'var y = "hello";',
    ],
    '7': [
      'let [name, age] = ["bob", 11];',
      'let z = a = b;',
    ],
    '8': [
      'y = foo(1, 2, 3);',
      'y = 10 + 5;',
    ],
  }

  for name, jsprogs in jss.items():
    ast_trees = [ast_parse.parse_text_dbg_no_text(jsp, 'js')[0] for jsp in jsprogs]
    trees = [DuoGlotTree(ast_tree) for ast_tree in ast_trees]
    unified_ast_tree = _unify_trees(trees)
    with open(f'temporary_test_unify_trees_{name}.json', 'w') as fout:
      fout.write(json.dumps(unified_ast_tree))


def _test_post_process_program_pairs():
  data = {
    "program_pairs": [
      {
        "source": "def f_gold(x: float, n: int) -> int:\n    return n",
        "target": "function f_gold(x, n) {\n    return n;\n}"
      }
    ],
    "contexts": [
      {
        "source_context": {
          "siblings": [],
          "parents": [
            "\"py.parameters\"",
            "\"py.function_definition\""
          ]
        },
        "target_context": {
          "siblings": [],
          "parents": [
            "\"js.formal_parameters\"",
            "\"js.function_declaration\""
          ]
        }
      }
    ]
  }

  result = post_process_program_pairs(data)
  print(result)


if __name__ == '__main__':
  # _test_post_process_generated_code_blocks_v3()
  _test_post_process_translation_pair()
