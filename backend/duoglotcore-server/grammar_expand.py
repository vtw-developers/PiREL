import cython
import sys
if cython.compiled: print("[grammar_expand] Compiled.", file=sys.stderr)
else: print("[grammar_expand] Interpreted.", file=sys.stderr)
####################################

import traceback
import timeit
import grammar_dlmparser as gdp
import grammar_rules
import consts
from consts import DEBUG_VERBOSE, NormalException, UnderstoodException, TranslationRuleNotFoundException
import copy
import ast_pretty
import sys
import json
import ast_parse
import p_data_structures as pds
from typing import Union, List
import p_templates
import p_utils
import logging


logger = logging.getLogger(__name__)


###################################################################
TRANS_VERBOSE : cython.int = DEBUG_VERBOSE


# ~~~ class that performs translation
class TransSession():

  def __init__(
    self,
    source_code,  # str, source code of source program
    source_ast,  # list[str, int, list[*]|str], AST of source program
    source_ann,  # dict, boundaries of AST nodes
    source_language_name,  # str, e.g. 'py'
    target_language_name,  # str, e.g. 'js'
    target_grammar,  # dict, grammar for target program in some internal representation
    program_str,  # str, raw text of translation rules ~~~
    optional_dbg_info_save_func,  # function, ?
    slot_dedup_enabled  # bool, ?
  ):

    # ~~~ this is a critical constant
    self._BACKWARD_MAX_STEP: cython.int = 100

    self._SNAPSHOT_INTERVAL: cython.int = 800
    self._SLOT_DEDUP_ENABLED: cython.bint = slot_dedup_enabled

    # the slot_dedup is only enabled for astnode choices for now.
    # step choices cannot use slot_dedup unless the cache is not on slots, but on slots' ranges.
    # current impl caches a one-to-one mapping from ranges to slots.

    # Okay to expose
    self.source_code = source_code
    self.source_ast = source_ast
    self.source_ann = source_ann
    self.source_language_name = source_language_name
    self.target_language_name = target_language_name
    self.target_grammar = target_grammar
    self.expansion_programs = []  # a list of expansion programs (~~~ a.k.a. translation rules)
    self.program_dbg_info = {
      "expansion_programs": []
    }

    # internals
    self._optional_dbg_info_save_func = optional_dbg_info_save_func
    self._counter_expansion_id: cython.int = 0
    self._counter_slot_id: cython.int = 1
    self._counter_alt_id: cython.int = 1

    self._slot_dict = {
      0: gdp.Slot(
        0,                         # slot_id:      int, index of slot (auto-increment, primary key)
        None,                      # belong_ex_id: int, index of parent slot
        ([self.source_ast], 0, 1)  # range_cursor: Tuple[ [slot AST] , start_inx, end_idx ]
      )
    }

    self._slot_dedup_lookup = {}
    self._slot_expand_info_dict = {} # no direct access

    # is only modified in self._get_or_create_alt_node()
    self._alt_tree_dict = {
      0: self._alt_node_as_dict(
        0,  # alt_id
        0,  # alt_step
        None,  # expansion
        None,  # choose_idx
        None,  # prev_alt_id
        [0],  # todo_slot_ids
        {"count": 0, "done": False},  # next_choices_status
        {},  # next_alt_choose_dict
        False,  # is_all_rejected
        True  # is_checkpoint
      )
    }  # alt_id -> alt_node

    self._alt_parser_result_dict = {}

    self._alt_parser_dict = {
      0: gdp.DelimitedParser(
        None,  # clone_obj
        self._slot_dict[0].slot_id,  # initial_slot_id
        target_grammar["_initial_prod"],  # initial_prod
        target_grammar,  # grammar
        self.target_language_name,  # target_language_name
        self._optional_dbg_info_save_func  # optional_dbg_info_func
      )
    } # alt_id -> Parser

    self.any_error = False
    self._set_program_str(program_str)

    # TransSession instances internally use `expansion_programs` for translation programs
    # The field below is used only for debugging purposes and can be removed later
    self.translation_rules_str = program_str


  # relation:
  #  each slot belongs to an expansion
  #  a fixed list of slots belong to the same expansion
  #  each expansion belong to one slot
  #  multiple expansions can be alternatives of the same slot
  def get_translation(self, choices, auto_backward=True, **kwargs):
    '''
    ~~~
    This is the main method for performing translation.
    Returns a full translation for a given source program

    PARAMETERS:
    choices: ?
    auto_backward: ?

    LOCALS:
    current_alt_node_dict: dict ?
    next_alt_node_dict: dict ?
    par_alt_node_dict: dict ?
    '''

    _subject_name = kwargs['subject_name']
    logger.info(f'{_subject_name} Starting TransSession.get_translation()')

    # 1 `choices_dict`
    choice_type = choices["type"]
    if choice_type == "STEP":
      choices_dict = {x:y for x, y in choices["choices_list"]}
    elif choice_type == "ASTNODE":
      choices_dict = {tuple(x):y for x, y in choices["choices_list"]}

    # 2 inner function `_get_or_create_next_alt_inner_fun`
    def _get_or_create_next_alt_inner_fun(alt_node, **kwargs):
      if TRANS_VERBOSE > -10: print("# _get_or_create_next_alt_inner_fun. current_alt_node_dict:", alt_node)
      assert len(alt_node["todo_slot_ids"]) > 0
      slot_expan_idx = 0
      new_step = alt_node["alt_step"] + 1
      if choice_type == "STEP":
        if new_step in choices_dict:
          slot_expan_idx = choices_dict[new_step]
      elif choice_type == "ASTNODE":
        todo_slot_id = alt_node["todo_slot_ids"][0]
        todo_slot = self._slot_dict[todo_slot_id]
        ast_node, start_idx, end_idx = todo_slot.range_cursor
        if new_step == 1:
          assert len(ast_node) == 1
        else:
          # if (len(ast_node) < 2):
          #   print("Unexpected ast_node: ", ast_node, file=sys.stderr)
          #   assert "unexpected ast_node length." == 0
          ast_id = ast_node[1]
          if not isinstance(ast_id, int):
            print("Unexpected ast_id: ", ast_id, file=sys.stderr)
            assert "unexpected ast_id" == 0
          key = (ast_id, start_idx, end_idx)
          if key in choices_dict:
            slot_expan_idx = choices_dict[key]
      else:
        assert "Unknown choice_type" == 0

      # ~~~ this is an important invocation: get_translation() -> _get_or_create_next_alt_inner_fun -> _get_or_create_alt_node()
      next_alt_node_dict = self._get_or_create_alt_node(alt_node, slot_expan_idx, **kwargs)
      return next_alt_node_dict

    # 3 inner function `_get_nth_parent_inner_fun`
    def _get_nth_parent_inner_fun(alt_node, n):
      if alt_node is None: return None
      if n == 0: return alt_node
      return _get_nth_parent_inner_fun(self._alt_tree_dict[alt_node["prev_alt_id"]], n - 1)

    # 4 inner function `_backward_alt_next_choice_inner_func`
    allowed_backward_alt_step = 0
    def _backward_alt_next_choice_inner_func(alt_node, child_choose_idx):
      nonlocal allowed_backward_alt_step
      if auto_backward == False:
        raise NormalException("Rejection occurred and automatic backwarding is disabled.")
      allowed_backward_alt_step = max(allowed_backward_alt_step, alt_node["alt_step"] - self._BACKWARD_MAX_STEP)
      if alt_node["alt_step"] < allowed_backward_alt_step:
        raise NormalException("Automatic backwarding failed to find alternative choices. (back limit)")
      next_choices_status = alt_node["next_choices_status"]
      if child_choose_idx + 1 >= next_choices_status["count"] and next_choices_status["done"]:
        prev_alt_id = alt_node["prev_alt_id"]
        if prev_alt_id is None:
          raise NormalException("Automatic backwarding failed to find alternative choices. (back to root)")
        return _backward_alt_next_choice_inner_func(self._alt_tree_dict[prev_alt_id], alt_node["choose_idx"])
      else:
        new_ch_idx = child_choose_idx + 1
        if choice_type == "STEP":
          next_step = alt_node["alt_step"] + 1
          if TRANS_VERBOSE > -11: print(f"++++++ _backward_alt_func set to: (alt_id:{alt_node['alt_id']}) (next_step:{next_step}) (new_ch_idx:{new_ch_idx})")
          return alt_node, next_step, new_ch_idx
        elif choice_type == "ASTNODE":
          slot_id = alt_node["todo_slot_ids"][0]
          slot_range_cursor = self._slot_dict[slot_id].range_cursor
          next_range_key = (slot_range_cursor[0][1], slot_range_cursor[1], slot_range_cursor[2])
          if TRANS_VERBOSE > -11: print(f"++++++ _backward_alt_func set to: (alt_id:{alt_node['alt_id']}) (next_range_key:{next_range_key}) (new_ch_idx:{new_ch_idx})")
          return alt_node, next_range_key, new_ch_idx
        else:
          assert "Unsupported choice_type" == 0

    # 5 inner function `_get_alt_parser_result_inner_fun`
    def _get_alt_parser_result_inner_fun(alt_node):
      try:
        parser_result = self._ensure_parser_result(alt_node)
        if TRANS_VERBOSE > -10: print("# _get_or_create_next_alt_inner_fun PARSE is_acceptable:", parser_result["is_acceptable"], " is_done:", parser_result["is_done"])
        return parser_result["is_acceptable"], parser_result["stuck_slot_id"], parser_result["is_done"]
      except Exception as err:
        error_alt_parser_result = self._alt_parser_result_dict[alt_node["alt_id"]]
        assert error_alt_parser_result["is_error"]
        raise err

    current_alt_node_dict = self._alt_tree_dict[0]
    is_expand_loop_successful = False
    error_info = {"msg": None}

    # 6 expand loop
    try:
      MAX_LOOPCOUNT = 15000
      loop_count = 0
      last_checkpoint_step = 0

      while True:
        loop_count += 1
        assert loop_count < MAX_LOOPCOUNT, "MAX_LOOP_excedded"
        assert len(current_alt_node_dict["todo_slot_ids"]) > 0
        if TRANS_VERBOSE > -10: print(f"############## _expand_loop {loop_count} ... ")

        # ~~~ this is an important invocation (contains invocation of Pirel)
        next_alt_node_dict = _get_or_create_next_alt_inner_fun(current_alt_node_dict, **kwargs)
        assert next_alt_node_dict is not None, "How_to_deal_with_this_case"

        par_alt_node_dict = current_alt_node_dict
        current_alt_node_dict = next_alt_node_dict

        # ~~~ this is an important invocation
        is_acceptable, stucking_slot_id, is_done = _get_alt_parser_result_inner_fun(current_alt_node_dict)

        if not is_acceptable:
          expansion = current_alt_node_dict["expansion"]
          if TRANS_VERBOSE > -11: print(f"!!!!!!!!!! _expand_loop apply_expand_func FAILED on exid:{expansion.ex_id} (corres_slot_id:{expansion.corres_slot_id}). Backward...\n\n")
          # optimization block
          if par_alt_node_dict["alt_step"] - last_checkpoint_step > self._BACKWARD_MAX_STEP:
            nth_parent = _get_nth_parent_inner_fun(par_alt_node_dict, self._BACKWARD_MAX_STEP)
            if nth_parent is not None:
              self._update_alt_node_as_checkpoint(nth_parent["alt_id"])
              last_checkpoint_step = nth_parent["alt_step"]
          current_alt_node_dict, update_key, update_choose_idx = _backward_alt_next_choice_inner_func(par_alt_node_dict, current_alt_node_dict["choose_idx"])
          choices_dict[update_key] = update_choose_idx

        elif len(current_alt_node_dict["todo_slot_ids"]) == 0:
          assert is_done
          break

        else:
          # optimization block
          if par_alt_node_dict["alt_step"] - last_checkpoint_step > self._SNAPSHOT_INTERVAL:
            self._update_alt_node_as_checkpoint(par_alt_node_dict["alt_id"])
            last_checkpoint_step = par_alt_node_dict["alt_step"]
          expansion = current_alt_node_dict["expansion"]
          if TRANS_VERBOSE > -11: print(f"************** _expand_loop {loop_count} apply_expand_func SUCCEED on exid:{expansion.ex_id} (corres_slot_id:{expansion.corres_slot_id})\n\n")

      is_expand_loop_successful = True

    # 7 catch exceptions and update `error_info` accordingly
    except Exception as err:
      print("############## traceback ##############", file=sys.stderr)
      print(traceback.format_exc(), file=sys.stderr)
      print("################# err #################", file=sys.stderr)

      # ~~~ Pirel: include information about problematic node in `error_info`
      if isinstance(err, TranslationRuleNotFoundException):
        templates_dict: dict = err.get_templates_dict()
        error_info['msg'] = f'\n{_subject_name} TranslationRuleNotFoundException:\nno rule found for "{templates_dict["problematic_node_type"]}"'
        error_info['templates_dict'] = json.dumps(templates_dict)

      elif isinstance(err, AssertionError):
        error_msg = "[FATAL_ERROR] SERVER STATE MIGHT BE CORRUPTED. Please check the log. " + str(err) + "\n" + str(traceback.format_exc())
        error_info["msg"] = error_msg
        consts.HIT_UNEXPECTED_ERROR_MESSAGE = error_msg
        consts.HIT_UNEXPECTED_ERROR = True
      elif isinstance(err, NormalException):
        error_info["msg"] = "[NormalException] " + str(err) + " " + traceback.format_exc()
      elif isinstance(err, UnderstoodException):
        error_info["msg"] = "[UnderstoodException] " + str(err) + " " + traceback.format_exc()
      else:
        error_info["msg"] = "[UNEXPECTED_ERROR] " + str(type(err)) + "\n" + str(err) + "\n" + traceback.format_exc()

    # 8 return
    if is_expand_loop_successful:
      tar_ast = self._get_alt_partial_ast(current_alt_node_dict)
      return (is_expand_loop_successful, tar_ast, choices_dict, None,       self._get_alt_debug_history(current_alt_node_dict))
    else:
      return (is_expand_loop_successful, None,    choices_dict, error_info, self._get_alt_debug_history(current_alt_node_dict))


  def _get_or_create_alt_node(self, prev_alt_node, slot_expan_idx, **kwargs):
    '''
    call stack (most recent on top):
    _get_or_create_alt_node()       <- this
    _get_or_create_next_alt_inner_fun()
    get_translation()               # inside an expand loop
    '''
    if TRANS_VERBOSE > -10: print(f"_get_or_create_alt_node (prev_id:{prev_alt_node['alt_id']}) (se_idx:{slot_expan_idx}) ...")
    assert len(prev_alt_node["todo_slot_ids"]) > 0

    prev_alt_node_id = prev_alt_node["alt_id"]
    prev_alt_step = prev_alt_node["alt_step"]
    new_node_corres_slot_id = prev_alt_node["todo_slot_ids"][0]

    # 1 expansion does not exist (create and cache it)
    if slot_expan_idx not in prev_alt_node["next_alt_choose_dict"]:

      # 2 ~~~ get expansion
      # TODO: discriminate No expansion and bad selection. Or should this be handled by frontend?
      expansion = self._get_expansion_for_slot(new_node_corres_slot_id, slot_expan_idx)

      # 3 ~~~~~ Pirel entrypoint
      if expansion is None:
        templates_dict: dict = self.pirel_get_templates(new_node_corres_slot_id, slot_expan_idx, **kwargs)
        raise TranslationRuleNotFoundException(templates_dict)
        # raise NormalException(f'Translation rule not found for slot {new_node_corres_slot_id}')

      next_choices_status = self._get_expansions_stat_for_slot(new_node_corres_slot_id)
      assert "next_choices_status" in prev_alt_node
      prev_alt_node["next_choices_status"] = next_choices_status

      alt_node = self._alt_node_as_dict(
        self._counter_alt_id,  # alt_id
        prev_alt_step + 1,  # alt_step
        expansion,  # expansion
        slot_expan_idx,  # choose_idx
        prev_alt_node_id,  # prev_alt_id
        self._alt_calc_todo_slots(expansion, prev_alt_node),  # todo_slot_ids
        {"count": 0, "done": False},  # next_choices_status
        {},  # next_alt_choose_dict
        False,  # is_all_rejected
        False  # is_checkpoint
      )

      self._alt_tree_dict[alt_node["alt_id"]] = alt_node
      prev_alt_node["next_alt_choose_dict"][slot_expan_idx] = alt_node["alt_id"]
      self._counter_alt_id += 1

    return self._alt_tree_dict[prev_alt_node["next_alt_choose_dict"][slot_expan_idx]]


  # ~~~~~ our logic for extracting templates from AST
  def pirel_get_templates(self, slot_id: int, idx: int, **kwargs):
    '''
    slot_range_cursor:
    Tuple[ AST , start_idx , end_idx ]
    '''

    _subject_name = kwargs['subject_name']
    logger.info(f'{_subject_name} Starting PiREL template extraction.')
    p_utils.log_file_time(f'{_subject_name}_program_to_translate.{self.source_language_name}', self.source_code)
    p_utils.log_file_time(f'{_subject_name}_translation_rules.snart', self.translation_rules_str)

    # context information
    contexts = self.pirel_get_all_contexts(slot_id)
    p_utils.log_json_time(f'{_subject_name}_contexts_grammar_expand.json', contexts)

    # slot is pertinent to the node that cannot be translated
    slot = self._slot_dict[slot_id]
    slot_range_cursor = slot.range_cursor
    slot_child_node_ids = slot.slot_node_ids

    slot_ast = slot_range_cursor[0]  # this is a pure AST node as parsed by ast_parse.parse_text_dbg() OR a sub-node
    slot_start_idx = slot_range_cursor[1]
    slot_end_idx = slot_range_cursor[2]

    # 1. identify problematic node
    # idea: it is the first NT node in slot.range_cursor.ast[start_idx, end_idx]
    problem_node_ast = None
    for __cursor_idx in range(slot_start_idx, slot_end_idx):
      problem_node_ast = slot_ast[__cursor_idx]
      if problem_node_ast[1] in slot_child_node_ids:
        break

    # full AST information can be leveraged
    full_ast_w_text, ast_annotation = ast_parse.parse_text_dbg(self.source_code, self.source_language_name, keep_text=True)

    templates_dict = p_templates.extract_templates(
      problematic_ast=problem_node_ast,
      full_ast=self.source_ast,
      full_ast_text=full_ast_w_text,
      ast_annotation=ast_annotation,
      lang=self.source_language_name,
      contexts=contexts,
      **kwargs
    )
    templates_dict['src_lang'] = self.source_language_name
    templates_dict['tar_lang'] = self.target_language_name

    p_utils.log_json_time(f'{_subject_name}_ALL-TEMPLATES-grammar_expand.json', templates_dict)
    logger.info(f'{_subject_name} PiREL template extraction is complete.')

    return templates_dict


  def pirel_get_all_contexts(self, problematic_slot_id: int):
    '''return a list of unique contexts for problematic node'''

    # 1 get slot ids that are problematic and have the same node type and node id
    problematic_slot_ids = self.pirel_expand_unexpanded_slots_get_problematic_slot_ids(problematic_slot_id)

    # 2 collect unique contexts
    unique_contexts_dict = {}
    for problematic_slot_id in problematic_slot_ids:
      source_context, target_context, scptr, tcptr = self.pirel_get_contexts_for_slot(problematic_slot_id)
      hash_val = str(source_context) + str(target_context)
      if hash_val not in unique_contexts_dict:
        unique_contexts_dict[hash_val] = {
          'source_context': source_context,
          'target_context': target_context,
          'scptr': scptr,
          'tcptr': tcptr,
        }

    return list(unique_contexts_dict.values())


  def pirel_get_contexts_for_slot(self, problematic_slot_id: int):
    '''
    Return the context of problematic node.
    That is, the sequence of nodes from context node
    to problematic node (in pre-order traversal) for both
    source and target sides.
    This information is useful for post-processing a rule
    in such a way, that allows us to extract the rule
    for the problematic node only (chop-off the context info).

    NOTE this is an early version of the algorithm.
    It skips nodes in cases where the applied rules (expansion)
    are complex.

    PRE1: slot_id in self._slot_dict

    ==== updated docs below
    PRE: slot_id is id of slot with no expansions
    NOTE
    target_context starts with 'unknown', because this method is
    intended to be used with slot that were not expanded
    '''

    assert problematic_slot_id in self._slot_dict

    def _get_slot_by_id(idx: int) -> gdp.Slot:
      return self._slot_dict[idx]

    def _get_expansion_by_id(idx: int) -> gdp.Expansion:
      for _item in self._slot_expand_info_dict.values():
        assert len(_item) == 3
        _expansions, _, _ = _item
        for _exp in _expansions:
          if _exp.ex_id == idx:
            return _exp
      raise RuntimeError('Expansion not found, should not happen')

    def _get_node_type_from_slot(slot: gdp.Slot) -> str:
      slot_range_cursor = slot.range_cursor
      slot_child_node_ids = slot.slot_node_ids

      slot_ast = slot_range_cursor[0]
      slot_start_idx = slot_range_cursor[1]
      slot_end_idx = slot_range_cursor[2]

      node_ast = None
      for _cursor_idx in range(slot_start_idx, slot_end_idx):
        node_ast = slot_ast[_cursor_idx]
        if node_ast[1] in slot_child_node_ids:
          break
      assert node_ast is not None

      slot_type = node_ast[0]
      return slot_type

    def _get_source_target_paths(expansion: gdp.Expansion, previous_slot: gdp.Slot) -> list:
      assert previous_slot in expansion.slots

      # ".1", ".2", "*3", etc
      slot_name = expansion.slot_names[expansion.slots.index(previous_slot)]

      # extract context from rule
      rule_id = expansion.notes['rule_id']
      trans_rule = self.expansion_programs[rule_id]
      match_pattern = trans_rule['match']  # aka source pattern
      expand_pattern = trans_rule['expand']  # aka target pattern

      match_tree = pds.PatternTree(match_pattern, self.source_language_name)
      expand_tree = pds.PatternTree(expand_pattern, self.target_language_name)
      phnode_match = match_tree.get_node_with_type(slot_name)
      phnode_expand = expand_tree.get_node_with_type(slot_name)

      source_path = phnode_match.get_path_to_root_source(expansion)
      target_path = phnode_expand.get_path_to_root_target(expansion, self._slot_expand_info_dict)

      return source_path, target_path

    def _update_contexts(context: List[list], paths: list):
      for sibling in paths[-1]:
        context[-1].append(sibling)
      for parent in reversed(paths[:-1]):
        context.append(parent)

    def _update_contexts_per_trans_rule(context: List[list], paths: list):
      # parent of previous
      parents = []
      for e in reversed(paths[:-1]):
        parents.append([e[-1]])
      context.append(['parent', parents])

    source_context = []
    target_context = []
    source_context_per_trans_rule = []
    target_context_per_trans_rule = []

    # 1
    # Since we start with the problematic node,
    # obtain its type first.
    # The corresponding type in the target side is 'unknown',
    # because we don't know what problematic node converts to.

    problematic_slot : gdp.Slot = _get_slot_by_id(problematic_slot_id)
    problematic_slot_type : str = _get_node_type_from_slot(problematic_slot)

    # NOTE what if the slot is partially matched? -> get only the top node in rule
    # NOTE can problematic node have a sibling?
    source_context.append([problematic_slot_type])
    target_context.append(['unknown'])
    # NOTE these two are needed for better context construction:
    # for some cases, chain of parents may differ in length for source
    # and target contexts. Instead of blindly picking N parents above,
    # pick them based on (please read the source code, I am sorry)
    source_context_per_trans_rule.append(('init', [[problematic_slot_type]]))
    target_context_per_trans_rule.append(('init', [['unknown']]))

    # 2
    # set up transduction tree cursors
    # iterate up over slot-expansion pairs
    previous_slot = problematic_slot
    cursor_expansion_id : Union[int, None] = problematic_slot.belong_ex_id
    # hit the root node (unlikely at this step)
    if cursor_expansion_id is None:
      return source_context, target_context, source_context_per_trans_rule, target_context_per_trans_rule
    cursor_expansion = _get_expansion_by_id(cursor_expansion_id)
    cursor_slot_id = cursor_expansion.corres_slot_id
    cursor_slot = _get_slot_by_id(cursor_slot_id)

    # 3
    # iterating up the transduction tree
    while True:

      source_paths, target_paths = _get_source_target_paths(cursor_expansion, previous_slot)
      _update_contexts(source_context, source_paths)
      _update_contexts(target_context, target_paths)
      _update_contexts_per_trans_rule(source_context_per_trans_rule, source_paths)
      _update_contexts_per_trans_rule(target_context_per_trans_rule, target_paths)

      # update cursors
      previous_slot = cursor_slot
      cursor_expansion_id = cursor_slot.belong_ex_id
      # hit the root node
      if cursor_expansion_id is None:
        break
      cursor_expansion = _get_expansion_by_id(cursor_expansion_id)
      cursor_slot_id = cursor_expansion.corres_slot_id
      cursor_slot = _get_slot_by_id(cursor_slot_id)

    return source_context, target_context, source_context_per_trans_rule, target_context_per_trans_rule


  def pirel_expand_unexpanded_slots_get_problematic_slot_ids(self, problematic_slot_id: int):
    ''''''
    def _get_slot_root_node_id(slot: gdp.Slot) -> int:
      '''extract useful information from slot'''
      slot_range_cursor = slot.range_cursor
      slot_child_node_ids = slot.slot_node_ids

      slot_ast = slot_range_cursor[0]
      slot_start_idx = slot_range_cursor[1]
      slot_end_idx = slot_range_cursor[2]

      node_ast = None
      for _cursor_idx in range(slot_start_idx, slot_end_idx):
        node_ast = slot_ast[_cursor_idx]
        if node_ast[1] in slot_child_node_ids:
          break
      assert node_ast is not None

      slot_node_id = node_ast[1]
      return slot_node_id

    def _get_slot_root_node_type(slot: gdp.Slot) -> str:
      '''extract useful information from slot'''
      slot_range_cursor = slot.range_cursor
      slot_child_node_ids = slot.slot_node_ids

      slot_ast = slot_range_cursor[0]
      slot_start_idx = slot_range_cursor[1]
      slot_end_idx = slot_range_cursor[2]

      node_ast = None
      for _cursor_idx in range(slot_start_idx, slot_end_idx):
        node_ast = slot_ast[_cursor_idx]
        if node_ast[1] in slot_child_node_ids:
          break
      assert node_ast is not None

      slot_type = node_ast[0]
      return slot_type

    def _get_slot_parent_expansion(slot: gdp.Slot) -> Union[gdp.Expansion, None]:
      '''
      get parent expansion of slot (up)
      a slot belongs to exactly ONE expansion
      '''
      for expansions, is_finished, expansion_gen in self._slot_expand_info_dict.values():
        for expansion in expansions:
          if expansion.ex_id == slot.belong_ex_id:
            return expansion

      # reaching this line means we reached root slot (which has no parent expansion)
      return None

    def _get_slot_possible_expansions(slot: gdp.Slot) -> Union[List[gdp.Expansion], None]:
      '''
      return all possible expansions that might be created from this slot (down)

      might return
      1. None - in case expansions were not generated for this slot
      2. empty list - no translation rule matched for slot
      3. non-empty list - expansions
      '''

      slot_id = slot.slot_id

      # slot was created, but expansions for this slot were not
      if slot_id not in self._slot_expand_info_dict:
        return None

      return self._slot_expand_info_dict[slot_id][0]

    def _get_expansion_root_node_type(expansion: gdp.Expansion) -> str:
      ''''''
      expansion_fragment = expansion.expan_fragment

      # TODO changes depending on the size of expansion_fragment
      expansion_type = expansion_fragment[1][0].strip('"')

      return expansion_type

    def _get_expansion_parent_slot(expansion: gdp.Expansion) -> gdp.Slot:
      '''
      get the slot from which this expansion was created (up)
      an expansion can be created from exactly ONE slot
      '''
      parent_slot_id = expansion.corres_slot_id

      # TODO does it always exist?
      return self._slot_dict[parent_slot_id]

    def _get_expansion_created_slots(expansion: gdp.Expansion) -> List[gdp.Slot]:
      '''
      return a list of all slots that were created by this expansions
      the list might be empty. in fact, it is empty for translation rules that create
      only terminals on the target side
      '''
      # might contain None (in cases where a rule matches an empty AST)
      expansion_slots_all = expansion.slots
      expansion_slots = list(filter(lambda x: isinstance(x, gdp.Slot), expansion_slots_all))
      return expansion_slots

    def _traverse_expand_unexpanded_slots_down_and_collect_problematic_slots(slot: gdp.Slot, from_expansion: gdp.Expansion):
      '''
      when translation fails, complete generating expansions for all slots
      NOTE this has to be done, because when translation stops at a slot,
      some slots (to be precise, the ones that come after the problematic slot in
      pre-order traversal?) are kept unexpanded (i.e. no expansions are created
      from them)
      '''

      # 0 check if slot is problematic
      nonlocal problematic_slots
      nonlocal problematic_slot_node_type
      nonlocal problematic_slot_node_id
      if _get_slot_root_node_type(slot) == problematic_slot_node_type and _get_slot_root_node_id(slot) == problematic_slot_node_id:
        problematic_slots.append(slot)

      # 1 get all expansions for this slot
      slot_possible_expansions = _get_slot_possible_expansions(slot)

      # case 1: expansions were not created from this slot -> run `self._get_expansion_for_slot()`
      if slot_possible_expansions is None:
        slot_id : int = slot.slot_id
        slot_expan_idx = 0  # choose i-th in case of multiple expansions

        # NOTE might return None
        expansion = self._get_expansion_for_slot(slot_id, slot_expan_idx)

        if expansion is not None:
          _traverse_expand_unexpanded_slots_down_and_collect_problematic_slots(slot, from_expansion)

      # case 2: no translation rule to translate the slot -> can stop
      elif len(slot_possible_expansions) == 0:
        pass

      # case 3: iterate expansions
      else:
        for possible_expansion in slot_possible_expansions:

          # 2 get all slots created by `possible_expansion`
          possible_expansion_slots = _get_expansion_created_slots(possible_expansion)

          # 3 for each slot, recurse down
          for possible_expansion_slot in possible_expansion_slots:
            _traverse_expand_unexpanded_slots_down_and_collect_problematic_slots(possible_expansion_slot, possible_expansion)

    # NOTE not used here, for future reference
    def _traverse_slot_expansion_down(slot: gdp.Slot, expansion: gdp.Expansion):
      '''
      PARAMS
      slot:

      expansion:
      an expansion that was created from `slot`
      '''
      nonlocal all_path_segments

      # 1 do sth with `slot`
      # 2 do sth with `expansion`
      slot_node_type = _get_slot_root_node_type(slot)
      slot_node_id = _get_slot_root_node_id(slot)
      expansion_type = _get_expansion_root_node_type(expansion)
      slot_id = slot.slot_id
      expansion_id = expansion.ex_id
      all_path_segments.append(f'down s{slot_id}_{slot_node_type}_{slot_node_id} -> e{expansion_id}_{expansion_type}')

      # 3 get all slots created by `expansions` (down)
      expansion_slots = _get_expansion_created_slots(expansion)

      # 4 for each slot, get all possible expansions
      for expansion_slot in expansion_slots:
        expansion_slot_node_type = _get_slot_root_node_type(expansion_slot)
        expansion_slot_node_id = _get_slot_root_node_id(expansion_slot)
        expansion_slot_id = expansion_slot.slot_id
        possible_expansion_slot_expansions = _get_slot_possible_expansions(expansion_slot)

        # case 1: expansions were not created yet
        if possible_expansion_slot_expansions is None:
          all_path_segments.append(f'down s{expansion_slot_id}_{expansion_slot_node_type}_{expansion_slot_node_id} -> ?')
          continue

        # case 2: expansions were attempted
        if len(possible_expansion_slot_expansions) == 0:
          all_path_segments.append(f'down s{expansion_slot_id}_{expansion_slot_node_type}_{expansion_slot_node_id} -> x')
          continue

        for possible_expansion_slot_expansion in possible_expansion_slot_expansions:

          # for each [slot, expansion] pair, recurse
          _traverse_slot_expansion_down(expansion_slot, possible_expansion_slot_expansion)

    # NOTE not used here, for future reference
    def _traverse_slot_expansion_down_from_start():
      ''''''
      start_slot_id = 0
      start_slot = self._slot_dict[start_slot_id]
      possible_expansions = _get_slot_possible_expansions(start_slot)

      assert possible_expansions is not None
      assert len(possible_expansions) > 0

      for possible_expansion in possible_expansions:
        _traverse_slot_expansion_down(start_slot, possible_expansion)

    # NOTE not used here, for future reference
    def _traverse_slot_expansion_up(slot: gdp.Slot, from_expansion: Union[gdp.Expansion, None]):
      '''
      PARAMS
      from_expansion:
      an expansion from which we arrived at `slot` when going up.
      essentially, `from_expansion` is an expansion that was created from `slot`.

      TERMS
      parent_expansion
      grand_parent_slot
      '''
      nonlocal all_path_segments

      # 1 do sth with slot
      slot_node_type = _get_slot_root_node_type(slot)
      slot_node_id = _get_slot_root_node_id(slot)
      from_expansion_type = _get_expansion_root_node_type(from_expansion) if from_expansion is not None else 'x'
      slot_id = slot.slot_id
      from_expansion_id = from_expansion.ex_id if from_expansion is not None else ''
      all_path_segments.append(f'up s{slot_id}_{slot_node_type}_{slot_node_id} -> e{from_expansion_id}_{from_expansion_type}')

      # 4 get the expansion that this slot belongs to
      parent_expansion = _get_slot_parent_expansion(slot)

      # the `slot` is the root slot
      if parent_expansion is None:
        return

      # 5 get the slot from which parent_expansion was created
      grand_parent_slot = _get_expansion_parent_slot(parent_expansion)

      # 6 recurse into grand_parent_slot
      _traverse_slot_expansion_up(grand_parent_slot, parent_expansion)

    # 0 temporary list needed for some inner methods here
    # inner methods are stored for future reference, safe to remove now
    all_path_segments = []

    # 1 some information on problematic node
    problematic_slot : gdp.Slot = self._slot_dict[problematic_slot_id]
    problematic_slot_node_type : str = _get_slot_root_node_type(problematic_slot)
    problematic_slot_node_id : int = _get_slot_root_node_id(problematic_slot)
    problematic_slots : List[gdp.Slot] = []  # all slots that point to problematic node

    # 2 expand all unexpanded slots and collect problematic slots
    start_slot_id = 0
    start_slot : gdp.Slot = self._slot_dict[start_slot_id]
    _traverse_expand_unexpanded_slots_down_and_collect_problematic_slots(start_slot, None)

    # 3
    problematic_slot_ids = [slot.slot_id for slot in problematic_slots]
    return problematic_slot_ids


  def _get_expansion_for_slot(self, slot_id: int, idx: int) -> Union[None, gdp.Expansion]:
    '''
    ~~~ if this function returns None, it means that DuoGlot failed to find a rule for translation

    call stack (most recent on top):
    _get_expansion_for_slot()       <- this
    _get_or_create_alt_node()
    _get_or_create_next_alt_inner_fun()
    get_translation()               # inside an expand loop
    '''
    slot = self._slot_dict[slot_id]

    # 1 check cache
    if slot_id not in self._slot_expand_info_dict:
      self._slot_expand_info_dict[slot_id] = [
        [],  # expan_list
        False,  # is_done
        self._possible_expansion_iter_gen(slot)  # iterobj
      ]

    expan_list, is_done, iterobj = self._slot_expand_info_dict[slot_id]

    # 2 expansion exists in cache
    if idx < len(expan_list):
      return expan_list[idx]

    # TODO debug this location: when is it reached?
    if is_done:
      return None

    # 3 find all expansions
    MAX_NUM_ALTERNATIVE_EXPANSIONS = 10
    try:
      while len(expan_list) < idx + MAX_NUM_ALTERNATIVE_EXPANSIONS: # use +2
        next_expansion: gdp.Expansion = next(iterobj)
        assert next_expansion is not None
        expan_list.append(next_expansion)
    except StopIteration:
      self._slot_expand_info_dict[slot_id][1] = True
      self._slot_expand_info_dict[slot_id][2] = None

    # 4 requested expansion idx exists
    if idx < len(expan_list):
      return expan_list[idx]

    # 5 requested expansion idx doesn't exist
    return None


  def _possible_expansion_iter_gen(self, slot):
    if TRANS_VERBOSE > 0: print(f"_possible_expansion_iter_gen slot: ({slot})")

    choose_idx = 0
    # iterate over all translation rules (a.k.a. expansion programs) in a natural order (as provided in the text field)
    # if a rule matches a 'slot', get an Expansion object and yield it (generator)
    # generator is called in a loop
    # 3 is hard-coded in _get_expansion_for_slot()
    for rule_id in range(len(self.expansion_programs)):
      me_prog = self.expansion_programs[rule_id]
      ruletype = me_prog["type"]
      match = me_prog["match"]
      expand = me_prog["expand"]
      flag_dict = me_prog["flags"] if ruletype == "ext_match_expand" else None

      # try the matcher. If true, return an expansion object
      # expansion is either a None (no match for a given rule_id)
      #              OR     a gdp.Expansion (match exists)
      expansion = self._try_get_expansion_if_match_on_slot(
        slot,  # slot
        rule_id,  # rule_id
        ruletype,  # m_ruletype
        match,  # m_match
        expand,  # m_expand
        flag_dict,  # m_flag_dict
        {"choose_idx": choose_idx}  # notes
      )

      if expansion is not None:
        if TRANS_VERBOSE > 0: print("# _possible_expansion_iter_gen matched!", slot, expansion)
        yield expansion
        choose_idx += 1

    return None


  # if successful, this function should return an expand object
  def _try_get_expansion_if_match_on_slot(
    self,
    slot,
    rule_id,
    m_ruletype,
    m_match,
    m_expand,
    m_flag_dict,
    notes
  ):
    '''
    PARAMETERS:
    slot:       grammar_dlmparser.Slot
    rule_id:    int (natural index of translation rule in the ruleset, a.k.a. expansion_programs)
    m_ruletype: str (e.g. `match_expand`)
    m_match:    list (a type+rule that is matched against source AST)
    m_expand:   list (a type+rule that is matched against target AST)

    LOCALS:
    m_matcher: a source AST matching rule itself -> ['"py.module"', '"*"']

    ORIGINAL DOCS:
    print("_try_get_expansion_if_match_on_slot:", slot, m_match, m_expand)
    the range cursor is a cursor on a list of source nodes
    '''

    is_ext_ruletype = m_ruletype == "ext_match_expand"
    m_matcher = None
    m_range_cursor = slot.range_cursor

    if m_match[0] == "fragment":
      m_matcher = m_match[1:]
      # TODO: check if there's bug
    else:
      m_matcher = [m_match]

    matching_ids = []
    slot_cursors = []
    matching_values = []
    matching_strs = []
    matching_anynts = []
    matching_liststrs = []
    matching_annos = []

    # change range cursor to be a tuple (ast_node, start_idx, end_idx) end_idx is the length if cursor is all.
    def _try_match_rec_inner_fun(
      range_cursor,
      range_cursor_idx: cython.int,
      matcher,
      matcher_idx: cython.int
    ) -> cython.bint:
      '''
      PARAMETERS:
      range_cursor:             Slot.range_cursor           Tuple[ List[src_ast] , int , int ]
      range_cursor_idx:         int                         start index in the AST list
      matcher:                  list                        [['"py.argument_list"', '"*"'], '"*"']
      matcher_idx:              int                         index in the matcher

      LOCALS:
      current_matcher_elem:     list                        ['"py.argument_list"', '"*"']
      matcher_operator:         str                         '"py.argument_list"'  # with double quotes as in rules
      current_matcher_type:     str                         'py.argument_list'  # without double quotes

      returns bool
      '''

      # assert range_cursor[2] <= len(range_cursor[0])
      if range_cursor_idx >= range_cursor[2] and matcher_idx >= len(matcher):
        return True

      # 1 matcher element is empty
      if matcher_idx >= len(matcher):
        # the rest of the cursor must all be terminals
        for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
          visit_elem = range_cursor[0][visit_cur_idx]
          if isinstance(visit_elem, str): continue
          else: return False  # contains non terminal
        return True  # loop done. All of them are terminals.

      # 2 matcher element is not empty
      assert len(matcher) > 0
      current_matcher_elem = matcher[matcher_idx]

      # case 1 current_matcher_elem
      if current_matcher_elem == '"*"':
        # all the rest is a cursor
        slot_cursors.append((range_cursor[0], range_cursor_idx, range_cursor[2]))
        # nothing to update for matching ids
        return True

      # case 2 current_matcher_elem
      elif current_matcher_elem == '"."':
        # everything until the next NT is a cursor
        # everything after the next NT would be the rest to match
        split_idx = None
        visit_cur_idx : cython.int
        for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
          visit_elem = range_cursor[0][visit_cur_idx]
          if _is_elem_NT(visit_elem):
            split_idx = visit_cur_idx + 1
            break

        # NT not found
        if split_idx is None:
          return False

        # NT found, cursor endswith NT
        slot_cursors.append((range_cursor[0], range_cursor_idx, split_idx))
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          split_idx,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 3 current_matcher_elem
      elif current_matcher_elem == '"_val_"':
        assert len(matcher) == 1
        is_invalid = len(range_cursor[0]) != 3 or (range_cursor[2] - range_cursor[1]) != 1 or range_cursor_idx != 2
        if is_invalid:
          print("# UNEXPECTED range_cursor for _val_ match: ", range_cursor, range_cursor_idx)
          assert "UNEXPECTED range_cursor" == 0
        matching_values.append(range_cursor[0][2])
        return True

      # case 4 current_matcher_elem
      elif current_matcher_elem == '"_str_"':
        if range_cursor_idx >= range_cursor[2]:
          return False # TOCHECK: out of length is failed to match.
        current_range_elem = range_cursor[0][range_cursor_idx]
        if not isinstance(current_range_elem, str):
          return False
        matching_strs.append(current_range_elem)
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          range_cursor_idx + 1,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 5 current_matcher_elem
      elif current_matcher_elem == '"_liststr_"':
        assert is_ext_ruletype
        temp_rgcursor_idx : cython.int = range_cursor_idx
        temp_liststr = []
        while True:
          if temp_rgcursor_idx >= range_cursor[2]:
            break
          current_range_elem = range_cursor[0][temp_rgcursor_idx]
          if isinstance(current_range_elem, str):
            temp_liststr.append(current_range_elem)
            temp_rgcursor_idx += 1
          else:
            break
        matching_liststrs.append(temp_liststr)
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          temp_rgcursor_idx,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 6 current_matcher_elem
      elif current_matcher_elem == '"_anno_"':
        current_range_elem = range_cursor[0][range_cursor_idx]
        if not isinstance(current_range_elem, list):
          raise UnderstoodException("_anno_ meet none-annotation element: Not a list.")
        if current_range_elem[0] != "anno":
          raise UnderstoodException("_anno_ meet none-annotation element: elem head: " + current_range_elem[0])
        matching_annos.append(current_range_elem)
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          range_cursor_idx + 1,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 7 current_matcher_elem (non-terminal) not direct string, must be a list (all prev if's are False)
      assert isinstance(current_matcher_elem, list)
      matcher_operator = current_matcher_elem[0]

      # case 7.1
      if range_cursor_idx >= range_cursor[2]:
        if matcher_operator == "val" or matcher_operator == "str" or matcher_operator.startswith('"'):
          return False
        elif matcher_operator == "nostr":
          return _try_match_rec_inner_fun(
            range_cursor,  # range_cursor
            range_cursor_idx,  # range_cursor_idx
            matcher,  # matcher
            matcher_idx + 1  # matcher_idx
          )
        else:
          print("UNEXPECTED range_cursor_idx out of length (range):", range_cursor_idx, range_cursor, file=sys.stderr)
          print("UNEXPECTED range_cursor_idx out of length (matcher):", matcher_idx, matcher, file=sys.stderr)
          assert "UNEXPECTED range_cursor_idx out of length" == 0

      # case 7.2
      if matcher_operator == "val":
        assert len(current_matcher_elem) == 2
        match_val = current_matcher_elem[1]
        is_invalid = len(range_cursor[0]) != 3 or (range_cursor[2] - range_cursor[1]) != 1 or range_cursor_idx != 2
        if is_invalid:
          print("# UNEXPECTED range_cursor for val match: ", range_cursor, range_cursor_idx)
          assert "UNEXPECTED range_cursor for val match" == 0
        range_val = range_cursor[0][range_cursor_idx]
        if not isinstance(range_val, str) and not isinstance(range_val, int) and not isinstance(range_val, float):
          return False
        if str(range_val) == str(match_val):
          return True  # TODO: FUTURE OPTIMIZE
        return False

      # case 7.3
      elif matcher_operator == 'str':
        assert len(current_matcher_elem) == 2
        match_val = current_matcher_elem[1]
        should_be_str_val = range_cursor[0][range_cursor_idx]

        # @satbek: skip `anno` in range_cursor when it's matched by `str`
        # for reference: L0004 (leetcode), long rule
        if isinstance(should_be_str_val, list) and len(should_be_str_val) > 0 and should_be_str_val[0] == 'anno':
          return _try_match_rec_inner_fun(
            range_cursor,  # range_cursor
            range_cursor_idx + 1,  # range_cursor_idx
            matcher,  # matcher
            matcher_idx  # matcher_idx
          )

        if not isinstance(should_be_str_val, str):
          return False
        if str(should_be_str_val) != str(match_val):
          return False # TODO: Future optimize
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          range_cursor_idx + 1,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 7.4
      elif matcher_operator == "nostr":
        assert len(current_matcher_elem) == 1
        should_not_be_str_val = range_cursor[0][range_cursor_idx]
        if isinstance(should_not_be_str_val, str):
          return False
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          range_cursor_idx,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 7.5
      elif matcher_operator == "anno":
        should_be_anno = range_cursor[0][range_cursor_idx]
        if not isinstance(should_be_anno, list):
          raise UnderstoodException("(anno ...) meet none-annotation element: Not a list.")
        if should_be_anno[0] != "anno":
          raise UnderstoodException("(anno ...) meet none-annotation element: elem head: " + should_be_anno[0])
        if not self.is_anno_compatible(current_matcher_elem, should_be_anno):
          return False
        return _try_match_rec_inner_fun(
          range_cursor,  # range_cursor
          range_cursor_idx + 1,  # range_cursor_idx
          matcher,  # matcher
          matcher_idx + 1  # matcher_idx
        )

      # case 7.6 not special operators, must be grammar NT constructs
      if not matcher_operator.startswith('"'):
        print("# Unknown operator in _try_match_rec_inner_fun. expecting NT constructs:", matcher_operator, file=sys.stderr)
        assert False

      current_matcher_type = matcher_operator[1:-1] # TODO: future optimize
      assert current_matcher_type != "fragment" and current_matcher_type != "anno"

      for visit_cur_idx in range(range_cursor_idx, range_cursor[2]):
        visit_elem = range_cursor[0][visit_cur_idx]

        # this is not an NT. It is a T. We are currently matching against an NT.
        if isinstance(visit_elem, str):
          continue
        # we are currently matching against NT. anno if not caputured in earlier cases, in this case it will be skipped.
        if visit_elem[0] == "anno":
          continue

        assert _is_elem_NT(visit_elem)
        visit_type = _get_elem_NT_type(visit_elem)
        is_direct_match = visit_type == current_matcher_type
        is_arbitrarynt_match = current_matcher_type == "_anynt_"

        # match
        if is_direct_match or (is_arbitrarynt_match and is_ext_ruletype):
          if is_direct_match and TRANS_VERBOSE > 0: print("_try_match_rec_inner_fun MATCHED! nice.", visit_type)
          if is_arbitrarynt_match:
            assert is_ext_ruletype, "ONLY_EXT_RULES_SUPPORT_ARBITRARY_MATCH"
            if TRANS_VERBOSE > 0: print("_try_match_rec_inner_fun ARBITRARY MATCHED! nice.", visit_type)
            matching_anynts.append(f'"{visit_type}"')

          # type match. add matching id.
          matching_ids.append(visit_elem[1])

          # check if the matching element is matched
          children_matcher = current_matcher_elem[1:] # TODO: optimize
          is_elem_matching = _try_match_rec_inner_fun(
            (visit_elem, 2, len(visit_elem)),  # range_cursor
            2,  # range_cursor_idx
            children_matcher,  # matcher
            0  # matcher_idx
          )

          if not is_elem_matching:
            return False

          return _try_match_rec_inner_fun(
            range_cursor,  # range_cursor
            visit_cur_idx + 1,  # range_cursor_idx
            matcher,  # matcher
            matcher_idx + 1  # matcher_idx
          )

        # mismatch
        if TRANS_VERBOSE > 0: print("_try_match_rec_inner_fun mismatch:", visit_type, current_matcher_type)
        return False

      # no match or mismatch
      return False
    # end of _try_match_rec_inner_fun()

    # try match rec
    is_matched = _try_match_rec_inner_fun(
      m_range_cursor,  # range_cursor
      m_range_cursor[1],  # range_cursor_idx
      m_matcher,  # matcher
      0  # matcher_idx
    )

    # ~~~ block of code for debugging DuoGlot match-expand algorithm
    # can safely be removed or commented out
    # if is_matched:
    #   try:
    #     import time
    #     current_time = time.time_ns()
    #     with open(f'temporary_match_expand_{current_time}_{is_matched}.json', 'w') as fout:
    #       fout.write(json.dumps({
    #         'range_cursor': m_range_cursor[0][m_range_cursor[1]:],
    #         'match': m_match,
    #         'expand': m_expand
    #       }))
    #   except IndexError:
    #     pass

    if TRANS_VERBOSE > -10 and is_matched: print("# _try_match_on_range_cursor MATCH: ", "   cursor: ", TransSession._pretty_range_cursor(m_range_cursor), "   matcher: ", m_matcher, file=sys.stderr)

    # print("_try_match_on_range_cursor:", is_matched)
    if not is_matched:
      return None

    new_notes = copy.copy(notes)
    new_notes["rule_id"] = rule_id

    return self._create_expansion(
      slot.slot_id,  # corres_slot_id
      m_expand,  # m_expand
      matching_ids,  # matching_ids
      slot_cursors,  # slot_cursors
      matching_values,  # matching_values
      matching_strs,  # matching_strs
      matching_anynts,  # matching_anynts
      matching_liststrs,  # matching_liststrs
      matching_annos,  # matching_annos
      new_notes  # notes
    ) # notes (for human debugging) not implemented


  def is_anno_compatible(self, matcher_anno, intree_anno):
    # print("matcher_anno:", matcher_anno, file=sys.stderr)
    # print("intree_anno:", intree_anno, file=sys.stderr)
    # return True
    # FUTURE TODO: improve performance
    matcher_anno_dict = {x[0]:x[1] for x in matcher_anno[1:]}
    intree_anno_dict = {x[0]:x[1] for x in intree_anno[1:]}
    for key in matcher_anno_dict:
      if key not in intree_anno_dict: return False
      if matcher_anno_dict[key] != intree_anno_dict[key]: return False
    return True

  @classmethod
  def _pretty_range_cursor(cls, range_cursor):
    additional_info = []
    for idx in range(range_cursor[1], range_cursor[2]):
      cursor_elem = range_cursor[0][idx]
      if isinstance(cursor_elem, list) and len(cursor_elem) > 0:
        additional_info.append(str(cursor_elem[0]))
      elif isinstance(cursor_elem, str):
        additional_info.append("str:" + cursor_elem)
      elif isinstance(cursor_elem, int):
        additional_info.append("int:" + str(cursor_elem))
      else:
        print("# ERROR!", cursor_elem)
        assert False
    return f"(len={str(len(range_cursor[0]))} start={range_cursor[1]} end={range_cursor[2]} {additional_info}))"

  def _create_expansion(
    self,
    corres_slot_id,
    m_expand,
    matching_ids,
    slot_cursors,
    matching_values,
    matching_strs,
    matching_anynts,
    matching_liststrs,
    matching_annos,
    notes=None
  ):
    self._counter_expansion_id += 1
    return gdp.Expansion(
      self._counter_expansion_id,  # ex_id
      corres_slot_id,  # corres_slot_id
      m_expand,  # expand
      matching_ids,  # matching_node_ids
      slot_cursors,  # src_slot_cursors
      matching_values,  # matching_values
      matching_strs,  # matching_strs
      matching_anynts,  # matching_anynts
      matching_liststrs,  # matching_liststrs
      matching_annos,  # matching_annos
      lambda ex_id, cursor : self._create_or_get_slot(ex_id, cursor),  # slot_create_func
      notes  # notes
    )

  def _create_or_get_slot(self, belong_ex_id, range_cursor):
    ast_id = range_cursor[0][1]
    assert isinstance(ast_id, int)
    start_idx = range_cursor[1]
    end_idx = range_cursor[2]

    if self._SLOT_DEDUP_ENABLED:
      astid_dict = None
      if ast_id in self._slot_dedup_lookup:
        astid_dict = self._slot_dedup_lookup[ast_id]
        if (start_idx, end_idx) in astid_dict:
          return astid_dict[(start_idx, end_idx)]
      else:
        astid_dict = {}
        self._slot_dedup_lookup[ast_id] = astid_dict

    self._counter_slot_id += 1
    new_slot = gdp.Slot(self._counter_slot_id, belong_ex_id, range_cursor)
    self._slot_dict[self._counter_slot_id] = new_slot

    if self._SLOT_DEDUP_ENABLED:
      # add to cache
      astid_dict[(start_idx, end_idx)] = new_slot

    return new_slot


  def _get_expansions_stat_for_slot(self, slot_id):
    assert slot_id in self._slot_expand_info_dict
    expan_list, is_done, _ = self._slot_expand_info_dict[slot_id]
    return {"count":len(expan_list), "done":is_done}

  def _alt_node_as_dict(
    self,
    alt_id,
    alt_step,
    expansion,
    choose_idx,
    prev_alt_id,
    todo_slot_ids,
    next_choices_status,
    next_alt_choose_dict,
    is_all_rejected,
    is_checkpoint
  ):
    return {
      "alt_id": alt_id,
      "alt_step": alt_step,
      "expansion": expansion,
      "choose_idx": choose_idx,
      "prev_alt_id": prev_alt_id,
      "todo_slot_ids": todo_slot_ids,
      "next_choices_status": next_choices_status,
      "next_alt_choose_dict": next_alt_choose_dict,
      "is_all_rejected": is_all_rejected,
      "is_checkpoint": is_checkpoint
    }

  def _alt_calc_todo_slots(self, expansion: gdp.Expansion, prev_alt_node):
    # todo slot dedup impl here? If dedup is on for the whole transsession, then this expansion and its corresponding slot must be unique.
    # can unique expansion/slot produce duplicated children slots? Should be yes.
    # But can the duplicated children slots appear in the same transduction history?
    # (only slots/expansions along a specific transduction history is book-keeped in transducer)
    # Not possible in current transducer impl. because matches inside an expansion are exclusive.
    # If matches are not exclusive, [1] + 2   and [1 +] 2 can be slot 1:([1]) slot 2:([1 +]). Another expansion on slot 2 break it down to [1] and [+]
    # will be unaware that [1] is already handled.
    # If we keep duplicated todo slots, will they affect the transduction?
    old_todo_slot_ids = prev_alt_node["todo_slot_ids"]
    prepend_ids = [x.slot_id for x in expansion.slots if x is not None]
    return prepend_ids + old_todo_slot_ids[1:]


  def _ensure_parser_result(self, alt_node):
    '''
    make sure the parser result is set.
    NOTE: parser_result might be error
    TODO what this method does?
    '''

    alt_id = alt_node["alt_id"]

    # 1 exists in cache (@satbek)
    if alt_id in self._alt_parser_result_dict:
      return self._alt_parser_result_dict[alt_id]

    # 2 does not exist in cache (@satbek)
    try:
      # fetch the previous parser (move or clone from the last checkpoint and move) and run it
      prev_alt_id = alt_node["prev_alt_id"]
      fetched_parser = self._fetch_parser(prev_alt_id)
      expansion = alt_node["expansion"]

      # ~~~ main work
      is_accepted, dbg_info = fetched_parser.add_expansion_parse_until_stuck(expansion)

      parser_result = self._parser_result_as_dict(
        is_accepted,  # is_acceptable
        fetched_parser.last_time_parsing_done,  # is_done
        False,  # is_error
        dbg_info,  # dbg_info
        fetched_parser.last_time_stuck_slot_id  # stuck_slot_id
      )

      self._alt_parser_result_dict[alt_id] = parser_result
      self._alt_parser_dict[alt_id] = fetched_parser

      return parser_result

    except Exception as err:
      print("#################### _ensure_parser_result FAILED! ####################")
      self.any_error = True
      fetched_parser.dbg_print_tail_stack()
      err_dbg_info = fetched_parser._dbg_info_finish_for_ex_error()

      err_parser_result = self._parser_result_as_dict(
        False,  # is_acceptable
        False,  # is_done
        True,  # is_error
        err_dbg_info,  # dbg_info
        None  # stuck_slot_id
      )

      self._alt_parser_result_dict[alt_id] = err_parser_result
      raise err

  def _parser_result_as_dict(
    self,
    is_acceptable,
    is_done,
    is_error,
    dbg_info,
    stuck_slot_id
  ):
    return {
      "is_acceptable": is_acceptable,
      "is_done": is_done,
      "is_error": is_error,
      "dbg_info": dbg_info,
      "stuck_slot_id": stuck_slot_id,
    }


  def _update_alt_node_as_checkpoint(self, alt_id):
    alt_node = self._alt_tree_dict[alt_id]
    if alt_node["is_checkpoint"]: return
    parser = self._fetch_parser(alt_id)
    self._alt_parser_dict[alt_id] = parser
    alt_node["is_checkpoint"] = True
    print(f"!!! Updating (alt_id:{alt_id}) as checkpoint.")

  def _fetch_parser(self, alt_id):
    """assume the parsing result of alt_id is already available. We don't care. Return a parser"""
    assert alt_id == 0 or alt_id in self._alt_parser_result_dict
    alt_node = self._alt_tree_dict[alt_id]

    # 1 exists in cache (@satbek)
    if alt_id in self._alt_parser_dict and self._alt_parser_dict[alt_id] is not None:
      if alt_node["is_checkpoint"]:
        print("# _fetch_parser cloning from checkpoint:", alt_id)
        return self._alt_parser_dict[alt_id].clone()
      else:
        parser = self._alt_parser_dict[alt_id]
        self._alt_parser_dict[alt_id] = None
        return parser

    # 2 does not exist in cache (@satbek)
    assert not alt_node["is_checkpoint"]
    prev_id = alt_node["prev_alt_id"]
    assert prev_id is not None
    expansion = alt_node["expansion"]
    fetched_parser = self._fetch_parser(prev_id)
    is_accepted, _ = fetched_parser.add_expansion_parse_until_stuck(expansion)
    assert is_accepted
    assert fetched_parser.last_time_stuck_slot_id == self._alt_parser_result_dict[alt_id]["stuck_slot_id"]
    return fetched_parser

  def _get_alt_partial_ast(self, alt_node):
    alt_id = alt_node["alt_id"]
    assert alt_id in self._alt_parser_dict
    parser = self._alt_parser_dict[alt_id]
    elem_list = parser.get_current_elem_list()
    return ast_pretty.elem_list_to_mapanno_ast(elem_list)

  def _get_alt_debug_history(self, alt_node):
    # get dbg_debug_info from the chain of parents start from alt_node
    alt_debug_history = []
    while alt_node["alt_id"] != 0:
      alt_id = alt_node["alt_id"]
      dbg_info = self._alt_parser_result_dict[alt_id]["dbg_info"]
      range_cursor = self._slot_dict[alt_node["expansion"].corres_slot_id].range_cursor
      alt_step = alt_node["alt_step"]
      range_info = None
      if alt_step == 1:
        assert len(range_cursor[0]) == 1
      else:
        range_info = (range_cursor[0][1], range_cursor[1], range_cursor[2])
      alt_debug_history.append({
        "alt_step": alt_step,
        "range_info": range_info,
        "next_choices_status": alt_node["next_choices_status"] ,
        "dbg_info": dbg_info
      })
      alt_node = self._alt_tree_dict[alt_node["prev_alt_id"]]
    alt_debug_history = list(reversed(alt_debug_history))
    return alt_debug_history


  def _set_program_str(self, code_str):
    # parse the code, set self.expansion_programs
    print(f"\n\n++++++++++++++++++++++++++++++++++++++++ _set_program_str. {len(code_str)} ++++++++++++++++++++++++++++++++++++++++\n")
    expansion_programs, dbg_info = grammar_rules.parse_analyze_rules(code_str)
    self.expansion_programs = expansion_programs
    self.program_dbg_info["expansion_programs"] = dbg_info
    print("++++++++++++  set self.expansion_programs")

  def get_session_dbg_info(self):
    return {"program": self.program_dbg_info}


# end of class `TransSession`

############################# utils #############################
@cython.cfunc
@cython.inline
def _is_elem_NT(visit_elem) -> cython.bint:
  if not isinstance(visit_elem, list): return False
  if visit_elem[0] == "anno": return False
  assert visit_elem[0] != "fragment"
  assert isinstance(visit_elem[1], int)
  return True

@cython.cfunc
@cython.inline
def _get_elem_NT_type(visit_elem):
  return visit_elem[0]
