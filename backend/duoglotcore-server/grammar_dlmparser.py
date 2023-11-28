import cython
import sys
if cython.compiled: print("[grammar_dlmparser] Compiled.", file=sys.stderr)
else: print("[grammar_dlmparser] Interpreted.", file=sys.stderr)
####################################

import grammar
import util_traverse
import copy
import consts
import json


# ~~~ for debugging, can be removed later
import debugpy
def _breakpoint():
  debugpy.listen(('0.0.0.0', 4444))
  debugpy.wait_for_client()
  debugpy.breakpoint()


def _get_node_ids_from_range_cursor(range_cursor):
  '''
  Returns (AST) node id's of child nodes
  '''
  node_ids = []
  for idx in range(range_cursor[1], range_cursor[2]):
    elem = range_cursor[0][idx]
    if isinstance(elem, list):
      if elem[0] != "anno":
        node_id = elem[1]
        assert isinstance(node_id, int)
        node_ids.append(node_id)
  return node_ids


class Slot:
  '''
  a slot is a sequence of NT/T to be decided. If only one NT,
  if symbol can be decided, should just write it out.
  A slot is meant to be something that type cannot be decided.
  '''
  def __init__(self, slot_id, belong_ex_id, range_cursor):
    '''
    ATTRIBUTES
    slot_id:          int                                    -
    belong_ex_id:     int                                    -
    range_cursor:     Tuple[ List[src_ast] , int , int ]     -
    slot_node_ids:    List[ int ]                            - ids of child nodes
    '''
    self.slot_id = slot_id
    self.belong_ex_id = belong_ex_id
    self.range_cursor = range_cursor
    self.slot_node_ids = _get_node_ids_from_range_cursor(range_cursor)
    if consts.DEBUG_VERBOSE > -10: print("# Slot create:", self.slot_id, " belong_ex_id:", self.belong_ex_id)

  def __str__(self):
    return f"(Slot id:{self.slot_id} belong_ex:{self.belong_ex_id})"

  def __repr__(self):
    return f"(Slot id: {self.slot_id}, belong_ex: {self.belong_ex_id})"

  def serialize_as_dict(self):
    '''
    for debugging purposes
    '''
    return {
      'slot_id': self.slot_id,
      'belong_ex_id': self.belong_ex_id,
      'range_cursor': self.range_cursor,
      'slot_node_ids': self.slot_node_ids
    }


class Expansion:
  # A matching rule is a rule that:
  #   - pattern-matching on source tree, yield several list cursors.
  #   - assign list cursors to slots.
  #   - mark the pattern that matched the source as "matched".

  def __init__(
      self,
      ex_id,
      corres_slot_id,
      expand,
      matching_node_ids,
      src_slot_cursors,
      matching_values,
      matching_strs,
      matching_anynts,
      matching_liststrs,
      matching_annos,
      slot_create_func,
      notes=None
    ):

    assert len(matching_node_ids) > 0
    if consts.DEBUG_VERBOSE > -10: print("# Expansion create:", expand)

    self.ex_id = ex_id
    self.corres_slot_id = corres_slot_id
    self.matching_node_ids = matching_node_ids # for debugging
    self.src_slot_cursors = src_slot_cursors # for debugging
    expan_fragment, slot_names, slots = self._fill(
      ex_id,  # ex_id
      expand,  # expand
      src_slot_cursors,  # src_slot_cursors
      slot_create_func,  # slot_create_func
      matching_values,  # matching_values
      matching_strs,  # matching_strs
      matching_anynts,  # matching_anynts
      matching_liststrs,  # matching_liststrs
      matching_annos  # matching_annos
    )

    # an expan_fragment is a list of NTs/Slots. Each NT is a expan_fragment.
    self.expan_fragment = expan_fragment

    self.slot_names = slot_names
    self.slots = slots
    assert len(slot_names) == len(slots)

    self.notes = notes # for human to read
    # ===== things below might not be used =====
    self._slot_id_dict = {}
    for slot in slots:
      if slot is not None:
        self._slot_id_dict[slot.slot_id] = slot

  def __str__(self):
    return f"(Expansion ex:{self.ex_id}, corres:{self.corres_slot_id})"

  def __repr__(self):
    return f"(Expansion ex:{self.ex_id}, corres:{self.corres_slot_id})"

  def _fill(
    self,
    ex_id,
    expand,
    src_slot_cursors,
    slot_create_func,
    matching_values,
    matching_strs,
    matching_anynts,
    matching_liststrs,
    matching_annos
  ):
    # fill in value holes so that the expansion tree only has slots
    slot_names = []
    slots = []
    slot_idx = 0

    # get {"_val1_": ...}
    matching_val_dict = {}
    matching_str_dict = {}
    matching_anynt_dict = {}
    matching_liststr_dict = {}
    matching_anno_dict = {}
    for vidx in range(len(matching_values)):
      match_key = f'"_val{vidx + 1}_"'
      matching_val_dict[match_key] = matching_values[vidx]
    for sidx in range(len(matching_strs)):
      match_key = f'"_str{sidx + 1}_"'
      matching_str_dict[match_key] = matching_strs[sidx]
    for aidx in range(len(matching_anynts)):
      match_key = f'"_anynt{aidx + 1}_"'
      matching_anynt_dict[match_key] = matching_anynts[aidx]
    for lsidx in range(len(matching_liststrs)):
      match_key = f'"_liststr{lsidx + 1}_"'
      matching_liststr_dict[match_key] = matching_liststrs[lsidx]
    for anidx in range(len(matching_annos)):
      match_key = f'"_anno{anidx + 1}_"'
      matching_anno_dict[match_key] = matching_annos[anidx]

    def _replace_and_visitor_inner_fun(node):
      nonlocal slot_idx

      def _NT_count_inner_inner_fun(cursor):
        nt_count = 0
        for idx in range(cursor[1], cursor[2]):
          x = cursor[0][idx]
          if isinstance(x, list):
            if x[0] != "anno": nt_count += 1
          else: assert isinstance(x, str) or isinstance(x, int)
        return nt_count

      def _NT_get_single_inner_inner_fun(cursor):
        single_NT = None
        for idx in range(cursor[1], cursor[2]):
          x = cursor[0][idx]
          if isinstance(x, list):
            if x[0] != "anno":
              assert single_NT is None
              single_NT = x
          else: assert isinstance(x, str) or isinstance(x, int)
        return single_NT

      # node is `list`
      if isinstance(node, list):
        if node[0] in ["val", "str", "nostr"]:
          return True, False, False, None
        elif node[0] == "val_ast_id":
          # get ast_id as a val node
          assert len(node) == 2
          assert node[1].startswith('"@.') and node[1].endswith('"')
          refidx_in_name = int(node[1][3:-1])
          if refidx_in_name == 0:
            ast_id = self.matching_node_ids[0]
          else:
            assert refidx_in_name > 0 and refidx_in_name <= len(src_slot_cursors)
            refsrc_slot_cursor = src_slot_cursors[refidx_in_name - 1]
            single_NT = _NT_get_single_inner_inner_fun(refsrc_slot_cursor)
            assert single_NT is not None
            ast_id = single_NT[1]
          return False, True, False, ["val", f'"{str(ast_id)}"']
        else:
          assert node[0] == "fragment" or node[0].startswith('"')
          return False, False, False, None

      # node is `str`
      assert isinstance(node, str)

      if node.startswith('"_val'):
        if node not in matching_val_dict:
          print("# _fill _replace_and_visitor_inner_fun val NOT FOUND:", node, matching_val_dict)
          assert False
        return False, True, False, [node, matching_val_dict[node]] # just ['val', ...] should also work

      elif node.startswith('"_str'):
        if node not in matching_str_dict:
          print("# fill _replace_and_visitor_inner_fun str NOT FOUND:", node, matching_str_dict)
          assert False
        return False, True, False, [node, matching_str_dict[node]] # just ['str', ...] should also work

      elif node.startswith('"_anynt'):
        if node not in matching_anynt_dict:
          print("# fill _replace_and_visitor_inner_fun anynt NOT FOUND:", node, matching_anynt_dict)
          assert False
        return False, True, False, matching_anynt_dict[node] # copy-paste an nt_name

      elif node.startswith('"_liststr'):
        if node not in matching_liststr_dict:
          print("# fill _replace_and_visitor_inner_fun liststr NOT FOUND:", node, matching_liststr_dict)
          assert False
        return False, True, True, [["str", x] for x in matching_liststr_dict[node]] # [['str', ...], ['str', ...], ...]

      elif node.startswith('"_anno'):
        if node not in matching_anno_dict:
          print("# fill _replace_and_visitor_inner_fun anno NOT FOUND:", node, matching_anno_dict)
          assert False
        return False, True, False, matching_anno_dict[node]

      elif node.startswith('"*') or node.startswith('".'):
        idx_in_name = int(node[-2:-1])
        assert idx_in_name > 0 and idx_in_name <= len(src_slot_cursors)
        slot_names.append(node)
        src_slot_cursor = src_slot_cursors[idx_in_name - 1]
        if node.startswith('".'): assert (src_slot_cursor[2] - src_slot_cursor[1]) >= 1  # if replacer startswith '".', it MUST contains at least one NT.
        slot = None # if no NT left, regard it as empty
        if _NT_count_inner_inner_fun(src_slot_cursor) > 0:
          slot = slot_create_func(ex_id, src_slot_cursor)
        slots.append(slot)
        if slot is not None:
          return False, True, False, [node, slot.slot_id] # there is a slot needs expansion.
        else:
          return False, True, False, [node, "EMPTY"]

      else:
        assert node.find("*") < 0 # str is already processed. not str, has "*" is not expected!
        return False, False, False, None

    exp_fragment = copy.deepcopy(expand)
    fill_count = util_traverse.traverse_nested_list_replace(
      exp_fragment,  # nested_list
      _replace_and_visitor_inner_fun  # node_replacer_func
    )

    assert len(slot_names) == len(slots)
    if exp_fragment[0] != "fragment":
      assert exp_fragment[0][0] == '"'
      # exp_fragment = ["fragment", exp_fragment]

    if consts.DEBUG_VERBOSE > -10: print("# _fill copy-and-fill-expand fill_count:", fill_count, exp_fragment)

    return exp_fragment, slot_names, slots


# Principle: never modify a frame. Create a new frame instead.
# Frame references are copied around.
class DelimitedParser():

  def __init__(
    self,
    clone_obj,
    initial_slot_id,
    initial_prod,
    grammar,
    target_language_name,
    optional_dbg_info_func
  ):
    if clone_obj is not None:
      assert clone_obj._loop_idx == 0
      assert clone_obj._is_grm_back_tracking == False
      assert clone_obj._grm_back_tracking_NT_depth is None
      assert clone_obj.last_time_dbg_info is None
      assert clone_obj.last_time_parsing_done == False
      assert initial_slot_id is None
      assert initial_prod is None
      assert grammar is None
      assert target_language_name is None
      assert optional_dbg_info_func is None

    ######### Variables for each call to add_expansion_parse_until_stuck #########
    self._LOOP_LIMIT = 24000
    self._loop_idx = 0
    # if the stack is back tracking. If will backtrack until a choice.
    # Go to next choice or repeat will reset this flag.
    self._is_grm_back_tracking = False
    self._grm_back_tracking_NT_depth = None

    self._last_time_stuck_stacksize = 0 if clone_obj is None else clone_obj._last_time_stuck_stacksize
    self.last_time_dbg_info = None
    self.last_time_stuck_slot_id = None if clone_obj is None else clone_obj.last_time_stuck_slot_id
    self.last_time_parsing_done = False
    self._optional_dbg_info_func = optional_dbg_info_func if clone_obj is None else clone_obj._optional_dbg_info_func

    ######## Variables across different calls to add_expansion_parse_until_stuck #########
    # the stacked state of the continuations
    self._tail_stack = [[
      None, # newly create node in target language (if any)
      [], # list for detecting loops in grammar parsing
      self._expan_continuation_as_tuple(
        0,  # ex_nt_depth
        None,  # ex_id
        ['fragment', ['"*1"', initial_slot_id]],  # expan_fragment
        1,  # fragment_idx
        None  # expan_continuation
      ),
      self._grammar_continuation_as_tuple(
        0,  # grm_nt_depth
        None,  # par_node_id
        initial_prod,  # prod
        0,  # cho_idx
        0,  # seq_idx
        None  # grammar_continuation
      )
    ]] if clone_obj is None else copy.copy(clone_obj._tail_stack)

    self._elem_dict = {} if clone_obj is None else copy.copy(clone_obj._elem_dict)

    # dict of expansion and slot_id to expansion mapping
    self._expansion_dict = {} if clone_obj is None else copy.copy(clone_obj._expansion_dict)
    self._slot_id_to_expansion_dict = {} if clone_obj is None else copy.copy(clone_obj._slot_id_to_expansion_dict)

    # The internal variable used for getting unique node idx
    self._current_parse_node_idx = -1 if clone_obj is None else clone_obj._current_parse_node_idx
    # grammar, for NT prod lookup
    self.grammar = grammar if grammar is not None else clone_obj.grammar
    self.target_language_name = target_language_name if target_language_name is not None else clone_obj.target_language_name

    # debugging only, not copied.
    self._pretty_cache = {}
    self._ENABLE_PRETTY_CACHE = False
    self._IMMUTABLE_ASSERT = False
    self._ALL_CREATED_FRAMES = []
    self._IS_RECORDING_FRAME_CREATION = False
    self._VERBOSE = consts.DEBUG_VERBOSE

  def clone(self):
    return DelimitedParser(
      self,  # clone_obj
      None,  # initial_slot_id
      None,  # initial_prod
      None,  # grammar
      None,  # target_language_name
      None  # optional_dbg_info_func
    )

  def _set_grm_back_tracking(self, nt_depth, msg=None):
    if self._VERBOSE > -1: print(f"# _set_grm_back_tracking at depth ({nt_depth}) ....... ({msg})")
    self._is_grm_back_tracking = True
    self._grm_back_tracking_NT_depth = nt_depth

  def _clr_grm_back_tracking(self):
    self._is_grm_back_tracking = False
    self._grm_back_tracking_NT_depth = None

  def _symbol_to_prefixed_symbol(self, symbol_name):
    return self.target_language_name + "." + symbol_name

  def _prefixed_symbol_to_symbol(self, prefixed_symbol_name):
    splitted = prefixed_symbol_name.split(".")
    assert len(splitted) == 2
    return splitted[1]

  def _check_should_skip_symbol(self, symbol_name):
    return grammar.grm_is_skipped_NT(self.grammar, symbol_name)

  def _check_aliased_noncf_symbol(self, symbol_name):
    if symbol_name in self.grammar["_aliased_symbols"]: return True
    return False

  def dbg_print_tail_stack(self):
    # added by @satbekmyrza: entire tail stack
    for i in range(0, len(self._tail_stack)):
    # original: last 20 elements
    # for i in range(len(self._tail_stack) - 20, len(self._tail_stack)):
      print(self._pretty_frame_short(i, self._tail_stack[i]))

  def _add_expansion(self, expansion: Expansion):
    ex_id = expansion.ex_id
    corres_id = expansion.corres_slot_id
    assert ex_id is not None
    assert corres_id is not None
    if ex_id in self._expansion_dict:
      assert self._expansion_dict[ex_id] is expansion
    else:
      assert corres_id not in self._slot_id_to_expansion_dict
      self._expansion_dict[ex_id] = expansion
      self._slot_id_to_expansion_dict[corres_id] = expansion

  def _grammar_continuation_as_tuple(
    self,
    grm_nt_depth,
    par_node_id,
    prod,
    cho_idx,
    seq_idx,
    grammar_continuation
  ):
    # return [grm_nt_depth, par_node_id, prod, cho_idx, seq_idx, grammar_continuation]
    return (
      grm_nt_depth,
      par_node_id,
      prod,
      cho_idx,
      seq_idx,
      grammar_continuation
    )

  def _expan_continuation_as_tuple(
    self,
    ex_nt_depth,
    ex_id,
    expan_fragment,
    fragment_idx,
    expan_continuation
  ):
    # return [ex_nt_depth, ex_id, expan_fragment, fragment_idx, expan_continuation]
    return (
      ex_nt_depth,
      ex_id,
      expan_fragment,
      fragment_idx,
      expan_continuation
    )

  def _frame_as_tuple(
    self,
    node,
    loop_det_list,
    ex_contin,
    grm_contin
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_contin is None or len(grm_contin) == 6
    # return [node, loop_det_list, ex_contin, grm_contin]
    return (
      node,
      loop_det_list,
      ex_contin,
      grm_contin
    )

  def _get_nullified_rep_or_cho_frame(self, frame):
    assert len(frame) == 4
    grm_cont = frame[3]
    assert len(grm_cont) == 6
    prod = grm_cont[2]
    assert prod["type"] == "REPEAT" or prod["type"] == "CHOICE"
    # new_frame = [frame[0], frame[1], frame[2], [grm_cont[0], grm_cont[1], grm_cont[2], -1, grm_cont[4], grm_cont[5]]]
    new_frame = (
      frame[0],
      frame[1],
      frame[2],
      (
        grm_cont[0],
        grm_cont[1],
        grm_cont[2],
        -1,
        grm_cont[4],
        grm_cont[5]
      )
    )
    if self._VERBOSE > 0: print("@@@@@@@@  NULLIFY last frame grm nullified.", self._pretty_frame_short(-1, new_frame))
    return new_frame

  def _get_specified_rep_or_cho_frame(self, frame, cho_idx):
    assert len(frame) == 4
    grm_cont = frame[3]
    assert len(grm_cont) == 6
    prod = grm_cont[2]
    assert prod["type"] == "REPEAT" or prod["type"] == "CHOICE"
    # new_frame = [frame[0], frame[1], frame[2], [grm_cont[0], grm_cont[1], grm_cont[2], cho_idx, grm_cont[4], grm_cont[5]]]
    new_frame = (
      frame[0],
      frame[1],
      frame[2],
      (
        grm_cont[0],
        grm_cont[1],
        grm_cont[2],
        cho_idx,
        grm_cont[4],
        grm_cont[5]
      )
    )
    if self._VERBOSE > 0: print("$$$ _get_specified_rep_or_cho_frame cho_idx=", cho_idx, self._pretty_frame_short(-1, new_frame))
    return new_frame

  def _get_next_rep_or_cho_frame(self, frame):
    assert len(frame) == 4
    grm_cont = frame[3]
    assert len(grm_cont) == 6
    prod = grm_cont[2]
    assert prod["type"] == "REPEAT" or prod["type"] == "REPEAT1" or prod["type"] == "CHOICE"
    assert grm_cont[3] >= 0
    # new_frame = [frame[0], frame[1], frame[2], [grm_cont[0], grm_cont[1], grm_cont[2], grm_cont[3] + 1, grm_cont[4], grm_cont[5]]]
    new_frame = (
      frame[0],
      frame[1],
      frame[2],
      (
        grm_cont[0],
        grm_cont[1],
        grm_cont[2],
        grm_cont[3] + 1,
        grm_cont[4],
        grm_cont[5]
      )
    )
    if self._VERBOSE > 0: print("$$$ GETNEXT (for rep/cho) frame grm nexted:", grm_cont[3] + 1)
    if prod["type"] == "REPEAT": assert grm_cont[3] < 3
    return new_frame

  def _pretty_expan_cont(self, exc):
    if exc is None: return "None"
    expan_cont_str = None
    def _get_pretty_expan(exc):
      return f"(EXC ntdepth({exc[0]}) eid({exc[1]}) frag({exc[2]}) fidx({exc[3]})) => " +  self._pretty_expan_cont(exc[4])
    if self._ENABLE_PRETTY_CACHE and id(exc) in self._pretty_cache:
      expan_cont_str = self._pretty_cache[id(exc)]
      if self._IMMUTABLE_ASSERT and expan_cont_str != _get_pretty_expan(exc):
        if self._VERBOSE > 0: print("# _pretty_grammar_cont IMMUTABLE ASSUMPTION VIOLATED!", "\n", expan_cont_str, "\n", _get_pretty_expan(exc))
        assert 1 == 0
    else:
      expan_cont_str = _get_pretty_expan(exc)
      self._pretty_cache[id(exc)] = expan_cont_str
    return expan_cont_str

  def _pretty_grammar_cont(self, grc):
    if grc is None: return "None"
    grammar_cont_str = None
    def _get_pretty_grammar(grc):
      return f"(GRC ntdepth({grc[0]}) pid({grc[1]}) prod({id(grc[2]) if grc[2] is not None else ''} {grammar.grm_prod_pretty(grc[2])}) c_idx({grc[3]}) s_idx({grc[4]})) => " + self._pretty_grammar_cont(grc[5])
    if self._ENABLE_PRETTY_CACHE and id(grc) in self._pretty_cache:
      grammar_cont_str = self._pretty_cache[id(grc)]
      if self._IMMUTABLE_ASSERT and grammar_cont_str != _get_pretty_grammar(grc):
        if self._VERBOSE > 0: print("# _pretty_grammar_cont IMMUTABLE ASSUMPTION VIOLATED!", "\n", grammar_cont_str, "\n", _get_pretty_grammar(grc))
        assert 1 == 0
    else:
      grammar_cont_str = _get_pretty_grammar(grc)
      self._pretty_cache[id(grc)] = grammar_cont_str
    return grammar_cont_str

  def _pretty_frame(self, frame_idx, frame):
    assert len(frame) == 4
    assert frame[2] is None or len(frame[2]) == 5
    assert frame[3] is None or len(frame[3]) == 6
    exc = frame[2]
    grc = frame[3]
    expan_cont_str = self._pretty_expan_cont(exc)
    grammar_cont_str = self._pretty_grammar_cont(grc)
    return str(frame_idx) + ". " + str(frame[0]) + "  |  " + str(frame[1]) + "  \\\\\\  " + expan_cont_str  + "  ///  " + grammar_cont_str

  def _pretty_frame_short(self, frame_idx, frame):
    assert len(frame) == 4
    assert frame[2] is None or len(frame[2]) == 5
    assert frame[3] is None or len(frame[3]) == 6
    exc = frame[2]
    grc = frame[3]
    expan_cont_str = self._pretty_expan_cont(exc)
    grammar_cont_str = self._pretty_grammar_cont(grc)
    expan_cont_str = expan_cont_str.split(" => ")[0] + " =>..." if expan_cont_str != "None" else "None"
    grammar_cont_str = grammar_cont_str.split(" => ")[0] + " =>..." if grammar_cont_str != "None" else "None"

    # added by @satbekmyrza
    is_print_tabulized = True  # prints the tail stack with fixed size columns
    if is_print_tabulized:
      return f'{str(frame_idx):<5} . {str(frame[0]):<100} | {str(frame[1]):<100} \\\\\\ {expan_cont_str:<500} /// {grammar_cont_str:<500}'
    else:
      # original
      return str(frame_idx) + ". " + str(frame[0]) + "  |  " + str(frame[1]) + "  \\\\\\  " + expan_cont_str  + "  ///  " + grammar_cont_str

  def _pretty_last_frame(self):
    frame_idx = len(self._tail_stack) - 1
    frame = self._tail_stack[-1]
    return self._pretty_frame(frame_idx, frame)

  def _pretty_last_frame_short(self):
    frame_idx = len(self._tail_stack) - 1
    frame = self._tail_stack[-1]
    return self._pretty_frame_short(frame_idx, frame)

  def _get_unique_node_id(self):
    self._current_parse_node_idx += 1
    return self._current_parse_node_idx

  # 1/2 of methods appending to tail stack
  def _commit_tail_call(
    self,
    added_node,
    loop_det_list,
    ex_cont,
    grm_cont
  ):
    assert ex_cont is None or len(ex_cont) == 5
    assert grm_cont is None or len(grm_cont) == 6
    # new_frame = [added_node, loop_det_list, ex_cont, grm_cont]
    new_frame = (
      added_node,
      loop_det_list,
      ex_cont,
      grm_cont
    )
    if self._IS_RECORDING_FRAME_CREATION:
      self._ALL_CREATED_FRAMES.append(new_frame)
    self._tail_stack.append(new_frame)

  # 2/2 of methods appending to tail stack
  def _just_tail_call(
    self,
    loop_det_list,
    ex_cont,
    grm_cont
  ):
    assert ex_cont is None or len(ex_cont) == 5
    assert grm_cont is None or len(grm_cont) == 6
    # new_frame = [None, loop_det_list, ex_cont, grm_cont]
    new_frame = (
      None,
      loop_det_list,
      ex_cont,
      grm_cont
    )
    if self._IS_RECORDING_FRAME_CREATION:
      self._ALL_CREATED_FRAMES.append(new_frame)
    self._tail_stack.append(new_frame)

  def _tail_frame_replace_with(self, replaced_frame):
    if self._IS_RECORDING_FRAME_CREATION:
      self._ALL_CREATED_FRAMES.append(replaced_frame)
    self._tail_stack[-1] = replaced_frame

  def _node_as_tuple(
    self,
    node_id,
    par_node_id,
    node_type,
    ntinfo_or_val,
    ex_id
  ):
    """node_type: T or NT"""
    newnode = (node_id, par_node_id, node_type, ntinfo_or_val, ex_id)
    self._elem_dict[id(newnode)] = newnode
    return newnode

  def _add_NT_tail(
    self,
    ex_nt_depth,
    ex_id,
    par_expan_fragment,
    elem_frag_idx,
    elem_expan_fragment,
    ex_contin,
    grm_nt_depth,
    par_node_id,
    nt_name,
    nt_prod,
    grm_contin
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_contin is None or len(grm_contin) == 6

    nt_node_id = self._get_unique_node_id()

    nt_node = self._node_as_tuple(
      nt_node_id,  # node_id
      par_node_id,  # par_node_id
      "NT",  # node_type
      [nt_name, None],  # ntinfo_or_val
      ex_id  # ex_id
    )

    ex_after_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      ex_id,  # ex_id
      par_expan_fragment,  # expan_fragment
      elem_frag_idx + 1,  # fragment_idx
      ex_contin  # expan_continuation
    )

    ex_elem_contin = self._expan_continuation_as_tuple(
      ex_nt_depth + 1,  # ex_nt_depth
      ex_id,  # ex_id
      elem_expan_fragment,  # expan_fragment
      1,  # fragment_idx
      ex_after_contin  # expan_continuation
    )

    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth + 1,  # grm_nt_depth
      nt_node_id,  # par_node_id
      nt_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_contin  # grammar_continuation
    )

    self._commit_tail_call(
      nt_node,  # added_node
      [],  # loop_det_list
      ex_elem_contin,  # ex_cont
      grm_contin  # grm_cont
    ) # the loop_det will reset on NT match

    if self._VERBOSE > -1: print(">> _add_NT_tail:", nt_name, f"ex_nt_depth: {ex_nt_depth} -> {ex_nt_depth+1}", self._pretty_last_frame_short())
    # if nt_name.find("_expression") >= 0: print(">> _add_NT_tail binary_expression:", nt_name, self._pretty_last_frame_short())

  def _add_match_str_tail(
    self,
    loop_det_list,
    par_node_id,
    str_value,
    ex_nt_depth,
    ex_id,
    expan_fragment,
    cur_fragment_idx,
    next_ex_contin,
    is_immediate,
    next_grm_contin
  ):
    assert next_ex_contin is None or len(next_ex_contin) == 5
    assert next_grm_contin is None or len(next_grm_contin) == 6

    t_node = self._node_as_tuple(
      None,  # node_id
      par_node_id,  # par_node_id
      "IT" if is_immediate else "T",  # node_type
      str_value,  # ntinfo_or_val
      ex_id  # ex_id
    )

    ex_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      ex_id,  # ex_id
      expan_fragment,  # expan_fragment
      cur_fragment_idx + 1,  # fragment_idx
      next_ex_contin  # expan_continuation
    )

    self._commit_tail_call(
      t_node,  # added_node
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      next_grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _add_match_str_tail:", str_value, self._pretty_last_frame_short())

  def _add_str_tail(
    self,
    loop_det_list,
    par_node_id,
    t_value,
    ex_cont,
    is_immediate,
    next_grm_cont
  ):
    assert ex_cont is None or len(ex_cont) == 5
    assert next_grm_cont is None or len(next_grm_cont) == 6

    t_node = self._node_as_tuple(
      None,  # node_id
      par_node_id,  # par_node_id
      "IT" if is_immediate else "T",  # node_type
      t_value,  # ntinfo_or_val
      None  # ex_id
    )

    self._commit_tail_call(
      t_node,  # added_node
      loop_det_list,  # loop_det_list
      ex_cont,  # ex_cont
      next_grm_cont  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _add_str_tail:", t_value, self._pretty_last_frame_short())

  def _add_external_tail(
    self,
    loop_det_list,
    par_node_id,
    t_value,
    ex_cont,
    next_grm_cont
  ):
    assert ex_cont is None or len(ex_cont) == 5
    assert next_grm_cont is None or len(next_grm_cont) == 6

    t_node = self._node_as_tuple(
      None,  # node_id
      par_node_id,  # par_node_id
      "EXT",  # node_type
      t_value,  # ntinfo_or_val
      None  # ex_id
    )

    self._commit_tail_call(
      t_node,  # added_node
      loop_det_list,  # loop_det_list
      ex_cont,  # ex_cont
      next_grm_cont  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _add_external_tail:", t_value, self._pretty_last_frame_short())

  def _add_match_val_tail(
    self,
    loop_det_list,
    ex_nt_depth,
    ex_id,
    par_expan_fragment,
    elem_frag_idx,
    next_expan_contin,
    par_node_id,
    t_value,
    is_immediate,
    next_grm_cont
  ):
    assert next_expan_contin is None or len(next_expan_contin) == 5
    assert next_grm_cont is None or len(next_grm_cont) == 6

    t_node = self._node_as_tuple(
      None,  # node_id
      par_node_id,  # par_node_id
      ("IV" if is_immediate else "V"),  # node_type
      t_value,  # ntinfo_or_val
      ex_id  # ex_id
    )

    ex_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      ex_id,  # ex_id
      par_expan_fragment,  # expan_fragment
      elem_frag_idx + 1,  # fragment_idx
      next_expan_contin  # expan_continuation
    )

    self._commit_tail_call(
      t_node,  # added_node
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      next_grm_cont  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _add_match_val_tail:", t_value, self._pretty_last_frame_short())

  def _inlined_prod_tail(
    self,
    loop_det_list,
    expan_continuation,
    grm_nt_depth,
    par_node_id,
    real_prod,
    next_grm_continuation
  ):
    assert expan_continuation is None or len(expan_continuation) == 5
    assert next_grm_continuation is None or len(next_grm_continuation) == 6

    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      real_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      next_grm_continuation  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      expan_continuation,  # ex_cont
      grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _inlined_prod_tail:", self._pretty_last_frame_short())

  def _prec_prod_tail(
    self,
    loop_det_list,
    expan_continuation,
    grm_nt_depth,
    par_node_id,
    prec_type,
    prec_value,
    inner_prod,
    next_grm_continuation
  ):
    assert expan_continuation is None or len(expan_continuation) == 5
    assert next_grm_continuation is None or len(next_grm_continuation) == 6

    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      inner_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      next_grm_continuation  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      expan_continuation,  # ex_cont
      grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _prec_prod_tail:", prec_type, prec_value, self._pretty_last_frame_short())

  def _field_prod_tail(
    self,
    loop_det_list,
    expan_contin,
    grm_nt_depth,
    par_node_id,
    field_prod,
    next_grm_contin
  ):
    assert expan_contin is None or len(expan_contin) == 5
    assert next_grm_contin is None or len(next_grm_contin) == 6

    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      field_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      next_grm_contin  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      expan_contin,  # ex_cont
      grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _field_prod_tail:", self._pretty_last_frame_short())

  def _seq_tail(
    self,
    loop_det_list,
    ex_contin,
    grm_nt_depth,
    par_node_id,
    current_prod,
    seq_prod,
    new_seq_idx,
    grm_continuation
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_continuation is None or len(grm_continuation) == 6

    grm_contin_after_current = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      seq_prod,  # prod
      0,  # cho_idx
      new_seq_idx,  # seq_idx
      grm_continuation  # grammar_continuation
    )

    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      current_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_contin_after_current  # grammar_continuation
    )
    # new_loop_det_list = loop_det_list if new_seq_idx > 0 else loop_det_list + [id(seq_prod)]

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _seq_tail:", self._pretty_last_frame_short())

  def _cho_trycurrent_tail(
    self,
    loop_det_list,
    ex_contin,
    grm_nt_depth,
    par_node_id,
    current_prod,
    grm_continuation
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_continuation is None or len(grm_continuation) == 6

    grm_contin_after_current = grm_continuation
    grm_contin = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      current_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_contin_after_current  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      grm_contin  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _cho_trycurrent_tail:", self._pretty_last_frame_short())

  def _rep_tryone_tail(
    self,
    loop_det_list,
    ex_contin,
    grm_nt_depth,
    par_node_id,
    one_prod,
    whole_repeat_prod,
    grm_continuation
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_continuation is None or len(grm_continuation) == 6

    grm_contin_after_try = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      whole_repeat_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_continuation  # grammar_continuation
    )

    grm_contin_tryone = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      one_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_contin_after_try  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      grm_contin_tryone  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _rep_tryone_tail:", self._pretty_last_frame_short())

  def _rep1_tryone_tail(
    self,
    loop_det_list,
    ex_contin,
    grm_nt_depth,
    par_node_id,
    one_prod,
    whole_repeat_prod,
    grm_continuation
  ):
    assert ex_contin is None or len(ex_contin) == 5
    assert grm_continuation is None or len(grm_continuation) == 6

    grm_contin_after_try = self._grammar_continuation_as_tuple(\
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      whole_repeat_prod,  # prod
      10,  # cho_idx
      0,  # seq_idx
      grm_continuation  # grammar_continuation
    )

    grm_contin_tryone = self._grammar_continuation_as_tuple(
      grm_nt_depth,  # grm_nt_depth
      par_node_id,  # par_node_id
      one_prod,  # prod
      0,  # cho_idx
      0,  # seq_idx
      grm_contin_after_try  # grammar_continuation
    )

    self._just_tail_call(
      loop_det_list,  # loop_det_list
      ex_contin,  # ex_cont
      grm_contin_tryone  # grm_cont
    )

    if self._VERBOSE > 0: print(">> _rep1_tryone_tail:", self._pretty_last_frame_short())

  def _wildcard_goto_expansion_tail_replace(
    self,
    cur_last_frame_node,
    loop_det_list,
    ex_nt_depth,
    cur_ex_id,
    cur_fragment,
    cur_fragment_idx,
    next_ex_contin,
    insert_ex_id,
    insert_fragment,
    grm_contin
  ):
    assert next_ex_contin is None or len(next_ex_contin) == 5
    assert grm_contin is None or len(grm_contin) == 6

    ex_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      insert_ex_id,  # ex_id
      insert_fragment,  # expan_fragment
      1,  # fragment_idx
      self._expan_continuation_as_tuple(  # expan_continuation
        ex_nt_depth,  # ex_nt_depth
        cur_ex_id,  # ex_id
        cur_fragment,  # expan_fragment
        cur_fragment_idx + 1,  # fragment_idx
        next_ex_contin  # expan_continuation
      )
    )
    # self._tail_frame_replace_with([cur_last_frame_node, loop_det_list, ex_contin, grm_contin])
    self._tail_frame_replace_with((cur_last_frame_node, loop_det_list, ex_contin, grm_contin))
    if self._VERBOSE > 0: print(">> _wildcard_goto_expansion_tail_replace:", self._pretty_last_frame_short())

  def _expansion_skip_elem_tail_replace(
    self,
    cur_last_frame_node,
    loop_det_list,
    ex_nt_depth,
    cur_ex_id,
    cur_fragment,
    skipping_fragment_idx,
    next_ex_contin,
    grm_contin
  ):
    assert next_ex_contin is None or len(next_ex_contin) == 5
    assert grm_contin is None or len(grm_contin) == 6

    ex_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      cur_ex_id,  # ex_id
      cur_fragment,  # expan_fragment
      skipping_fragment_idx + 1,  # fragment_idx
      next_ex_contin  # expan_continuation
    )
    # self._tail_frame_replace_with([cur_last_frame_node, loop_det_list, ex_contin, grm_contin])
    self._tail_frame_replace_with((cur_last_frame_node, loop_det_list, ex_contin, grm_contin))
    if self._VERBOSE > 0: print(">> _expansion_skip_elem_tail_replace:", self._pretty_last_frame_short())

  def _expansion_anno_elem_tail_replace(
    self,
    cur_last_frame_node,
    loop_det_list,
    ex_nt_depth,
    cur_ex_id,
    cur_fragment,
    anno_fragment_idx,
    next_ex_contin,
    grm_contin
  ):
    assert next_ex_contin is None or len(next_ex_contin) == 5
    assert grm_contin is None or len(grm_contin) == 6
    assert cur_fragment[anno_fragment_idx][0] == "anno"
    assert cur_last_frame_node is not None
    assert cur_last_frame_node[2] == "NT"

    new_last_frame_node = self._node_as_tuple(
      cur_last_frame_node[0],  # node_id
      cur_last_frame_node[1],  # par_node_id
      cur_last_frame_node[2],  # node_type
      [cur_last_frame_node[3][0], cur_fragment[anno_fragment_idx]],  # ntinfo_or_val
      cur_ex_id  # ex_id
    )

    ex_contin = self._expan_continuation_as_tuple(
      ex_nt_depth,  # ex_nt_depth
      cur_ex_id,  # ex_id
      cur_fragment,  # expan_fragment
      anno_fragment_idx + 1,  # fragment_idx
      next_ex_contin  # expan_continuation
    )

    # self._tail_frame_replace_with([new_last_frame_node, loop_det_list, ex_contin, grm_contin])
    self._tail_frame_replace_with((new_last_frame_node, loop_det_list, ex_contin, grm_contin))
    if self._VERBOSE > 0: print(">> _expansion_anno_elem_tail_replace:", self._pretty_last_frame_short())

  def _is_possible_prod_for_ex_contin(self, ex_contin, prod):
    if ex_contin is None:
      return True

    if self._VERBOSE > -2: print("--- _is_possible_prod_for_ex_contin", "frag_idx:", ex_contin[3], ex_contin[2])
    if self._VERBOSE > -2: print("    --- PRETTY PROD:", grammar.grm_prod_pretty(prod))

    if grammar.SYM_AHEADSET_KEY not in prod:
      return True

    ahead_set = prod[grammar.SYM_AHEADSET_KEY]

    # the loop of checking all ex_contin under the same NT_depth
    checking_ex_contin = ex_contin
    checking_nt_depth = checking_ex_contin[0]
    while True:
      ex_nt_depth, _, expan_fragment, fragment_idx, next_ex_contin = checking_ex_contin
      if ex_nt_depth < checking_nt_depth:
        break
      assert ex_nt_depth == checking_nt_depth
      for idx in range(fragment_idx, len(expan_fragment)):
        fragment_elem = expan_fragment[idx]
        if isinstance(fragment_elem, list):
          if (fragment_elem[0] == "str" or fragment_elem[0].startswith('"_str')):
            assert len(fragment_elem) == 2
            expecting_ahead_elem = ("str", fragment_elem[1])
            if expecting_ahead_elem not in ahead_set:
              if self._VERBOSE > -2: print("_is_possible_prod_for_ex_contin ELEM MISSING. Can assert not possible.", fragment_elem)
              return False
          if self._VERBOSE > -2: print("_is_possible_prod_for_ex_contin ELEM ", fragment_elem)
        else:
          print("#WHAAAAAT? Unexpected fragment_elem type:", fragment_elem)
          assert False
      checking_ex_contin = next_ex_contin
    return True

  def _dbg_info_finish_common(self):
    # self._tail_stack[:]
    # NOTE: this is inaccurate mode. FUTURE_TODO: enable accurate mode
    self.last_time_dbg_info["elem_list_info_id"] = self._optional_dbg_info_func((self._tail_stack, len(self._tail_stack)), _tail_stack_length_to_elem_list)
    self.last_time_dbg_info["loop_count"] = self._loop_idx
    dbg_info = self.last_time_dbg_info
    self.last_time_dbg_info = None
    self._clr_grm_back_tracking()
    self._loop_idx = 0
    return dbg_info

  def _dbg_info_finish_for_ex_accepted(self):
    self.last_time_dbg_info["outcome"] = "AC"
    return self._dbg_info_finish_common()

  def _dbg_info_finish_for_ex_rejected(self):
    self.last_time_dbg_info["outcome"] = "RE"
    return self._dbg_info_finish_common()

  def _dbg_info_finish_for_ex_error(self):
    self.last_time_dbg_info["outcome"] = "ER"
    return self._dbg_info_finish_common()

  # ~~~
  def add_expansion_parse_until_stuck(self, expansion: Expansion):
    '''
    return: is_accepted, dbg_info
    '''
    assert self.last_time_dbg_info is None
    assert self._loop_idx == 0
    assert self._is_grm_back_tracking == False

    # clear dbg info
    self.last_time_dbg_info = {
      "ex_id": expansion.ex_id,
      "corres_slot_id": expansion.corres_slot_id,
      "src_matching_node_ids": expansion.matching_node_ids, # src
      "slot_src_matching_node_ids": [_get_node_ids_from_range_cursor(x) for x in expansion.src_slot_cursors], # src
      "notes": expansion.notes,
      "slot_names": expansion.slot_names, # target
      "slot_ids": [(x.slot_id if x is not None else None) for x in expansion.slots], # target
    }

    if self._VERBOSE > 0: print("===============================")
    if self._VERBOSE > 0: print("# add_expansion_parse_until_stuck.", expansion)

    self._add_expansion(expansion)
    # current_stucking_slot_id = expansion.corres_slot_id
    # new_expan_fragment = expansion.expan_fragment

    # main loop
    while True:
      self._loop_idx += 1
      assert self._loop_idx <= self._LOOP_LIMIT, "LOOP_LIMIT_REACHED"
      if self._VERBOSE > 0: print("\n", "++++++++++++++++++++++++++++++++++++++++++", self._loop_idx, " _tail_stack:", len(self._tail_stack), "++++++++++++++++++++++++++++++++++++++++++")

      # ~~~ for debugging
      if self._loop_idx in [-99]:
        print("----------dbg_print_tail_stack start-------------")
        self.dbg_print_tail_stack()
        print("---------- dbg_print_tail_stack end -------------")

      # 1 grammar is backtracking
      if self._is_grm_back_tracking:
        # failed to parse
        if len(self._tail_stack) == 0:
          if self._VERBOSE > 0: print("add_expansion_parse_until_stuck FAILED TO PARSE.")
          return False, self._dbg_info_finish_for_ex_rejected()

        # can keep doing backtracking
        bk_node, _, _, bk_grm_contin = self._tail_stack[-1]
        if bk_grm_contin is None:
          self._tail_stack.pop()
          continue

        bk_grm_nt_depth, _, bking_prod, _, _, _ = bk_grm_contin
        prod_type = bking_prod["type"]
        if self._VERBOSE > 0: print(f"BACKTRACKING CHECKING ------(at grm_nt_depth {bk_grm_nt_depth})-------", grammar.grm_prod_pretty(bking_prod), bk_grm_contin[3], bk_grm_contin[4])
        assert self._grm_back_tracking_NT_depth >= 0 # TODO: not checked

        if bk_grm_nt_depth != self._grm_back_tracking_NT_depth:
          if self._VERBOSE > -1: print(f"# Backtracking.POP SKIP for depth {bk_grm_nt_depth} != {self._grm_back_tracking_NT_depth}")
        elif (prod_type == "CHOICE" or prod_type == "REPEAT" or prod_type == "REPEAT1") and bk_grm_contin[3] >= 0:
          # change to the next choice and clear back_tracking
          replacing_frame = self._get_next_rep_or_cho_frame(self._tail_stack[-1])
          self._tail_frame_replace_with(replacing_frame)
          if self._VERBOSE > 0: print("BACKTRACKING.NEXT:", prod_type, bk_grm_contin[3], "->", self._tail_stack[-1][3][3])
          self._clr_grm_back_tracking()
          continue
        else:
          # !!!! NOTE don't check the production symbol. Check the NT node instead.
          # !!!! The production symbol is not matched and is frequently backtracking.
          # PURPOSE: check if this is a **MATCHED** symbol is a not-skipping context-free NT symbol
          if bk_node is not None and bk_node[2] == "NT":
            symbol_name = self._prefixed_symbol_to_symbol(bk_node[3][0][1:-1])
            assert not self._check_should_skip_symbol(symbol_name)
            if not self._check_aliased_noncf_symbol(symbol_name):
              # CF symbol. Backtracking is not allowed. Return as error
              assert bk_grm_nt_depth == self._grm_back_tracking_NT_depth
              if self._VERBOSE > -11: print(f"# Backtracking TERMINATED. Meet Context-Free symbol ({symbol_name}) of the specified NT depth ({bk_grm_nt_depth}). Backtracking to such symbol indicates syntax errors.")
              return False, self._dbg_info_finish_for_ex_rejected()
            else:
              # non-CF symbol. backtracking is allowed. Update allowed _grm_back_tracking_NT_depth
              self._grm_back_tracking_NT_depth = self._grm_back_tracking_NT_depth - 1
              if self._VERBOSE > -1: print(f"BACKTRACKING.POP {bk_grm_nt_depth}  MATCHED_NT ALIASED NON-CF:", symbol_name, f"_grm_back_tracking_NT_depth {self._grm_back_tracking_NT_depth + 1} -> {self._grm_back_tracking_NT_depth}")
          elif bk_node is not None:
            if self._VERBOSE > -1: print("BACKTRACKING.POP NODE ", bk_grm_nt_depth, bk_node)
          else:
            if self._VERBOSE > 0: print("BACKTRACKING.POP ", bk_grm_nt_depth)

        # continue backtracking
        if not (len(self._tail_stack) >= self._last_time_stuck_stacksize):
          if self._VERBOSE > 0: print("# WARNING: BACKTRACKING < _last_time_stuck_stacksize:", len(self._tail_stack), self._last_time_stuck_stacksize)
        self._tail_stack.pop()
        continue

      # 2 grammar is not backtracking
      if self._VERBOSE > 0: print(self._pretty_last_frame_short())
      cur_last_frame_node, cur_loop_det_list, cur_ex_contin, cur_grm_contin = self._tail_stack[-1]

      # unpack cur_ex_contin
      ex_nt_depth, ex_id, expan_fragment, fragment_idx, next_ex_contin = cur_ex_contin if cur_ex_contin is not None else (None, None, None, None, None)
      fragment_item = expan_fragment[fragment_idx] if (cur_ex_contin is not None and fragment_idx < len(expan_fragment)) else None

      # 3 case 1
      if cur_ex_contin is None and cur_grm_contin is None:
        if self._VERBOSE > 0: print("# PARSING ALL SUCCESS.")
        self.last_time_stuck_slot_id = None
        self.last_time_parsing_done = True
        return True, self._dbg_info_finish_for_ex_accepted()

      # 4 case 2
      elif cur_ex_contin is not None and fragment_idx >= len(expan_fragment):
        assert fragment_idx >= 1
        assert fragment_idx == len(expan_fragment)
        if self._VERBOSE > 0: print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FINISH fragment.")
        self._tail_frame_replace_with(self._frame_as_tuple(
          cur_last_frame_node,  # node
          cur_loop_det_list,  # loop_det_list
          next_ex_contin,  # ex_contin
          cur_grm_contin  # grm_contin
        ))
        continue

      # 5 case 3
      elif cur_ex_contin is not None and (fragment_item[0].startswith('"*') or fragment_item[0].startswith('".')):
        inner_slot_id = fragment_item[1]
        if inner_slot_id == "EMPTY":
          assert not fragment_item[0].startswith('".')
          if self._VERBOSE > 0: print("# Skipping EMPTY slot at", fragment_idx, fragment_item)
          self._expansion_skip_elem_tail_replace(
            cur_last_frame_node,  # cur_last_frame_node
            cur_loop_det_list,  # loop_det_list
            ex_nt_depth,  # ex_nt_depth
            ex_id,  # cur_ex_id
            expan_fragment,  # cur_fragment
            fragment_idx,  # skipping_fragment_idx
            next_ex_contin,  # next_ex_contin
            cur_grm_contin  # grm_contin
          )
          continue
        elif inner_slot_id in self._slot_id_to_expansion_dict:
          inner_expansion = self._slot_id_to_expansion_dict[inner_slot_id]
          self._wildcard_goto_expansion_tail_replace(
            cur_last_frame_node,  # cur_last_frame_node
            cur_loop_det_list,  # loop_det_list
            ex_nt_depth,  # ex_nt_depth
            ex_id,  # cur_ex_id
            expan_fragment,  # cur_fragment
            fragment_idx,  # cur_fragment_idx, don't plus 1 for fragment_idx (handled inside _wildcard_goto_expansion_tail)
            next_ex_contin,  # next_ex_contin
            inner_expansion.ex_id,  # insert_ex_id
            inner_expansion.expan_fragment,  # insert_fragment
            cur_grm_contin  # grm_contin
          )
          continue
        else: # stuck is a good thing.
          assert isinstance(inner_slot_id, int)
          self._last_time_stuck_stacksize = len(self._tail_stack)
          self.last_time_stuck_slot_id = inner_slot_id
          if self._VERBOSE > 0: print("# Stuck!!! stacksize:", self._last_time_stuck_stacksize)
          return True, self._dbg_info_finish_for_ex_accepted()

      # 6 case 4
      elif cur_ex_contin is not None and fragment_item[0] == "anno":
        if self._VERBOSE > 0: print("# Add anno and continue:", fragment_idx, fragment_item)
        self._expansion_anno_elem_tail_replace(
          cur_last_frame_node,  # cur_last_frame_node
          cur_loop_det_list,  # loop_det_list
          ex_nt_depth,  # ex_nt_depth
          ex_id,  # cur_ex_id
          expan_fragment,  # cur_fragment
          fragment_idx,  # anno_fragment_idx
          next_ex_contin,  # next_ex_contin
          cur_grm_contin  # grm_contin
        )
        continue

      # 7 case 5
      elif cur_ex_contin is not None and cur_grm_contin is None:
        ###### NOTICE: The same piece of code also appears above ######
        ###### handle nostr matcher begin ######
        if isinstance(fragment_item, list) and fragment_item[0] == "nostr":
          # safe to skip nostr!!
          if self._VERBOSE > 0: print(f"# Safe to skip nostr !!! (cur_grm_contin is None: {cur_grm_contin})")
          assert len(fragment_item) == 1
          self._expansion_skip_elem_tail_replace(
            cur_last_frame_node,  # cur_last_frame_node
            cur_loop_det_list,  # loop_det_list
            ex_nt_depth,  # ex_nt_depth
            ex_id,  # cur_ex_id
            expan_fragment,  # cur_fragment
            fragment_idx,  # skipping_fragment_idx
            next_ex_contin,  # next_ex_contin
            cur_grm_contin  # grm_contin
          )
          continue
        else:
        ###### handle nostr matcher end ######
          self._set_grm_back_tracking(ex_nt_depth, "# CURRENT PARSING CANNOT FINISH EXPANSIONS. Backtracking.") # TODO: not tested
          continue

      # 8 case 6 this condition branch MUST progress in Grammar
      # unpack cur_grm_contin
      grm_nt_depth, par_node_id, prod, cho_idx, seq_idx, next_grm_contin = cur_grm_contin

      # expan_fragment is fine. now check grammar
      # NOTE cur_ex_contin might be none. next_grm_contin is not None.

      # check if this grammar depth is smaller than required
      if cur_ex_contin is not None and grm_nt_depth < ex_nt_depth:
        # an exception
        # NOTE The same piece of code also appears above
        # handle nostr matcher begin
        if isinstance(fragment_item, list) and fragment_item[0] == "nostr":
          # safe to skip nostr
          if self._VERBOSE > 0: print(f"# Safe to skip nostr !!! (grm_nt_depth {grm_nt_depth} < ex_nt_depth {ex_nt_depth})")
          assert len(fragment_item) == 1
          self._expansion_skip_elem_tail_replace(
            cur_last_frame_node,  # cur_last_frame_node
            cur_loop_det_list,  # loop_det_list
            ex_nt_depth,  # ex_nt_depth
            ex_id,  # cur_ex_id
            expan_fragment,  # cur_fragment
            fragment_idx,  # skipping_fragment_idx
            next_ex_contin,  # next_ex_contin
            cur_grm_contin  # grm_contin
          )
          continue
        else:
          self._set_grm_back_tracking(ex_nt_depth, f"# CURRENT PARSING DEPTH WRONG. ex:{ex_nt_depth} grm:{grm_nt_depth}. Backtracking." if self._VERBOSE > -1 else None)
          continue

      # might be at a state that backtracking will happen (grm_nt_depth > ex_nt_depth currently) or going on.
      prod_type = prod["type"]

      # prod_type case 1
      if prod_type == "SEQ":
        prod_members = prod["members"]
        if seq_idx >= len(prod_members):
          self._just_tail_call(
            cur_loop_det_list,  # loop_det_list
            cur_ex_contin,  # ex_cont
            next_grm_contin  # grm_cont
          )
        else:
          current_member_prod = prod_members[seq_idx]
          self._seq_tail(
            cur_loop_det_list,  # loop_det_list
            cur_ex_contin,  # ex_contin
            grm_nt_depth,  # grm_nt_depth
            par_node_id,  # par_node_id
            current_member_prod,  # current_prod
            prod,  # seq_prod
            seq_idx + 1,  # new_seq_idx
            next_grm_contin  # grm_continuation
          )

      # prod_type case 2
      elif prod_type == "CHOICE":
        prod_members = prod["members"]
        if cho_idx >= len(prod_members):
          if not cho_idx == len(prod_members):
            print("# ERROR: cho_idx invalid. cho_idx:", cho_idx, " len(prod_members):", len(prod_members))
            assert False
          self._tail_frame_replace_with(self._get_nullified_rep_or_cho_frame(self._tail_stack[-1]))
          self._set_grm_back_tracking(grm_nt_depth, f"CHOICE out of index {cho_idx}/{len(prod_members)}. nullified and backtracking." if self._VERBOSE > -1 else None)
        else:
          # find next cho_idx that is possible
          possible_cho_idx = cho_idx

          while possible_cho_idx < len(prod_members):
            member_prod = prod_members[possible_cho_idx]
            # if nt_depth mismatch, _is_possible_prod_for_ex_contin is not correct.
            if ex_nt_depth != grm_nt_depth:
              break
            if self._is_possible_prod_for_ex_contin(cur_ex_contin, member_prod):
              break
            possible_cho_idx += 1

          self._tail_frame_replace_with(self._get_specified_rep_or_cho_frame(self._tail_stack[-1], possible_cho_idx))

          if possible_cho_idx < len(prod_members):
            current_member_prod = prod_members[possible_cho_idx]
            self._cho_trycurrent_tail(
              cur_loop_det_list,  # loop_det_list
              cur_ex_contin,  # ex_contin
              grm_nt_depth,  # grm_nt_depth
              par_node_id,  # par_node_id
              current_member_prod,  # current_prod
              next_grm_contin  # grm_continuation
            )
          else:
            if self._VERBOSE > 0: print("# cho_idx exhausted. Expecting backtracking in the next round.")

      # prod_type case 3
      elif prod_type == "REPEAT":
        assert seq_idx == 0
        if cho_idx == 0:
          self._just_tail_call(
            cur_loop_det_list,  # loop_det_list
            cur_ex_contin,  # ex_cont
            next_grm_contin  # grm_cont
          )
        else:
          if cho_idx == 1:
            one_prod = prod["content"]
            self._rep_tryone_tail(
              cur_loop_det_list,  # loop_det_list
              cur_ex_contin,  # ex_contin
              grm_nt_depth,  # grm_nt_depth
              par_node_id,  # par_node_id
              one_prod,  # one_prod
              prod,  # whole_repeat_prod
              next_grm_contin  # grm_continuation
            )
          else:
            if cho_idx != 2:
              if self._VERBOSE > 0: print("# REPEAT UNEXPECTED ERROR CHO!", cho_idx, self._pretty_grammar_cont(cur_grm_contin))
            assert cho_idx == 2
            self._tail_frame_replace_with(self._get_nullified_rep_or_cho_frame(self._tail_stack[-1]))
            self._set_grm_back_tracking(grm_nt_depth, "REPEAT cho_idx == 2 No other shoice.")

      # prod_type case 4
      elif prod_type == "REPEAT1":
        assert seq_idx == 0
        if cho_idx == 0:
          one_prod = prod["content"]
          self._rep1_tryone_tail(
            cur_loop_det_list,  # loop_det_list
            cur_ex_contin,  # ex_contin
            grm_nt_depth,  # grm_nt_depth
            par_node_id,  # par_node_id
            one_prod,  # one_prod
            prod,  # whole_repeat_prod
            next_grm_contin  # grm_continuation
          )
        elif cho_idx == 1:
          self._tail_frame_replace_with(self._get_nullified_rep_or_cho_frame(self._tail_stack[-1]))
          self._set_grm_back_tracking(grm_nt_depth, "REPEAT1 cho_idx == 2 Head fail. No other shoice.")
        else:
          if cho_idx == 10:
            self._just_tail_call(
              cur_loop_det_list,  # loop_det_list
              cur_ex_contin,  # ex_cont
              next_grm_contin  # grm_cont
            )
          elif cho_idx == 11:
            one_prod = prod["content"]
            self._rep1_tryone_tail(
              cur_loop_det_list,  # loop_det_list
              cur_ex_contin,  # ex_contin
              grm_nt_depth,  # grm_nt_depth
              par_node_id,  # par_node_id
              one_prod,  # one_prod
              prod,  # whole_repeat_prod
              next_grm_contin  # grm_continuation
            )
          else:
            if cho_idx != 12:
              if self._VERBOSE > 0: print("# REPEAT1 UNEXPECTED ERROR CHO!", cho_idx, self._pretty_grammar_cont(cur_grm_contin))
            assert cho_idx == 12
            self._tail_frame_replace_with(self._get_nullified_rep_or_cho_frame(self._tail_stack[-1]))
            self._set_grm_back_tracking(grm_nt_depth, "REPEAT1 cho_idx == 12 No other shoice.")

      # prod_type case 5
      elif prod_type == "FIELD":
        field_prod = prod["content"]
        self._field_prod_tail(
          cur_loop_det_list,  # loop_det_list
          cur_ex_contin,  # expan_contin
          grm_nt_depth,  # grm_nt_depth
          par_node_id,  # par_node_id
          field_prod,  # field_prod
          next_grm_contin  # next_grm_contin
        )

      # prod_type case 6
      elif prod_type == "PREC" or prod_type == "PREC_LEFT" or prod_type == "PREC_RIGHT" or prod_type == "PREC_DYNAMIC":
        prec_type = prod_type
        prec_value = prod["value"]
        inner_prod = prod["content"]
        self._prec_prod_tail(
          cur_loop_det_list,  # loop_det_list
          cur_ex_contin,  # expan_continuation
          grm_nt_depth,  # grm_nt_depth
          par_node_id,  # par_node_id
          prec_type,  # prec_type
          prec_value,  # prec_value
          inner_prod,  # inner_prod
          next_grm_contin  # next_grm_continuation
        )

      # prod_type case 7
      elif prod_type == "SYMBOL" or prod_type == "ALIAS":
        # locally useful functions begin
        def _handle_matching_symbol_or_alias_inner_fun(expan_fragment_elem, symbol_name, alias_prod=None):
          if cur_ex_contin is None:
            # CHECK cur_ex_contin. if cur_ex_contin is None, there's no expan_fragment_elem
            assert expan_fragment_elem is None
            self._set_grm_back_tracking(grm_nt_depth, "symbol/alias nothing to match: expan_fragment_elem is None.")
            return
          if grm_nt_depth > ex_nt_depth:
            self._set_grm_back_tracking(grm_nt_depth, f"# _handle_matching_symbol_or_alias_inner_fun matching ({symbol_name}) grm_nt_depth > ex_nt_depth. ({grm_nt_depth} > {ex_nt_depth})" if self._VERBOSE > -1 else None)
            return
          if self._VERBOSE > 0: print("# symbol/aliased. expan_fragment_elem:", expan_fragment_elem, f"({fragment_idx} of parent)")
          assert isinstance(expan_fragment_elem, list)
          elem_nt_name = expan_fragment_elem[0]
          assert not elem_nt_name.startswith('"*')
          assert not elem_nt_name == 'fragment'
          if elem_nt_name == 'val' or elem_nt_name == 'str' or elem_nt_name.startswith('"_val') or elem_nt_name.startswith('"_str'):
            self._set_grm_back_tracking(grm_nt_depth, f"symbol/aliased current elem_nt_name is not NT, but val or str: {expan_fragment_elem} BACKTRACKING..." if (self._VERBOSE > -1) else None)
            return
          elif elem_nt_name == "nostr": # skip nostr.
            self._expansion_skip_elem_tail_replace(
              cur_last_frame_node,  # cur_last_frame_node
              cur_loop_det_list,  # loop_det_list
              ex_nt_depth,  # ex_nt_depth
              ex_id,  # cur_ex_id
              expan_fragment,  # cur_fragment
              fragment_idx,  # skipping_fragment_idx
              next_ex_contin,  # next_ex_contin
              cur_grm_contin  # grm_contin
            )
            return
          assert elem_nt_name.find(".") > 0
          t_symbol_name = f'"{self.target_language_name}.{symbol_name}"'
          if elem_nt_name == t_symbol_name:
            if self._VERBOSE > 0: print("symbol/aliased matching expand elem!", "ALIAS" if alias_prod is not None else "SYMBOL")
            symbol_or_alias_prod = grammar.grm_get_prod(self.grammar, symbol_name) if alias_prod is None else alias_prod
            self._add_NT_tail(
              ex_nt_depth,  # ex_nt_depth
              ex_id,  # ex_id
              expan_fragment,  # par_expan_fragment
              fragment_idx,  # elem_frag_idx
              expan_fragment_elem,  # elem_expan_fragment
              next_ex_contin,  # ex_contin
              grm_nt_depth,  # grm_nt_depth
              par_node_id,  # par_node_id
              elem_nt_name,  # nt_name
              symbol_or_alias_prod,  # nt_prod
              next_grm_contin  # grm_contin
            )
          else:
            if self._VERBOSE > 0: print()
            self._set_grm_back_tracking(grm_nt_depth, f"# symbol/aliased mismatch: {elem_nt_name} != {t_symbol_name}" if (self._VERBOSE > -1) else None)

        # locally useful functions end
        if prod_type == "SYMBOL":
          symbol_name = prod["name"]
          if self._check_should_skip_symbol(symbol_name):
            if not grammar.grm_is_external_NT(self.grammar, symbol_name):
              real_prod = grammar.grm_get_prod(self.grammar, symbol_name)
              self._inlined_prod_tail(
                cur_loop_det_list + [symbol_name],  # loop_det_list
                cur_ex_contin,  # expan_continuation
                grm_nt_depth,  # grm_nt_depth
                par_node_id,  # par_node_id
                real_prod,  # real_prod
                next_grm_contin  # next_grm_continuation
              )
            else:
              external_state_id, external_str = grammar.grm_external_NT_pretty_string(self.grammar, None, symbol_name)
              # TODO: handle external_state_id
              self._add_external_tail(
                cur_loop_det_list,  # loop_det_list
                par_node_id,  # par_node_id
                external_str,  # t_value
                cur_ex_contin,  # ex_cont
                next_grm_contin  # next_grm_cont
              )
          elif grammar.grm_is_external_NT(self.grammar, symbol_name):
            if symbol_name in self.grammar["rules"]:
              assert "is_fake" in self.grammar["rules"][symbol_name]
              _handle_matching_symbol_or_alias_inner_fun(fragment_item, symbol_name, None)
            else:
              print("# ERROR: unexpected external_NT, no fake prod:", symbol_name)
              assert 0 == "Unexpected_external_NT_no_fake_prod"
          else:
            _handle_matching_symbol_or_alias_inner_fun(fragment_item, symbol_name, None)

        else:
          assert prod_type == "ALIAS"
          if prod["named"]: # this is named. Naming a result of a prod as a symbol.
            alias_aim_symbol_name = prod["value"]
            alias_prod = prod["content"]
            # if the alias_prod is CHOICE or SYMBOL, no worry because the subprod is transformed so that SYMBOL will be jumped.
            assert not self._check_should_skip_symbol(alias_aim_symbol_name)
            _handle_matching_symbol_or_alias_inner_fun(fragment_item, alias_aim_symbol_name, alias_prod)
          else: # this is not named. the prod is acting as a scanner and scanning details are discarded. Only alias is in parse tree.
            # this should be treated as a string match. assume preprocessing is already putting a string prod at "pt_prod"
            assert "pt_content" in prod
            self._inlined_prod_tail(
              cur_loop_det_list,  # loop_det_list
              cur_ex_contin,  # expan_continuation
              grm_nt_depth,  # grm_nt_depth
              par_node_id,  # par_node_id
              prod["pt_content"],  # real_prod
              next_grm_contin  # next_grm_continuation
            )

      # prod_type case 8
      elif prod_type == "SYMBOL_JUMP":
        if self._VERBOSE > 0: print("meet SYMBOL_JUMP. prod name:", prod['name'])
        jump_prod = grammar.grm_get_prod(self.grammar, prod['name'])
        self._inlined_prod_tail(
          cur_loop_det_list + [prod['name']],  # loop_det_list
          cur_ex_contin,  # expan_continuation
          grm_nt_depth,  # grm_nt_depth
          par_node_id,  # par_node_id
          jump_prod,  # real_prod
          next_grm_contin  # next_grm_continuation
        )

      # prod_type case 9
      elif prod_type == "STRING":
        # check cur_ex_contin. It can be None.
        # if not None, then if current fragment_item is str, it should match.
        item_type = None
        # "immediate" key is added during preprocessing
        is_immediate = "immediate" in prod
        if cur_ex_contin is not None:
          assert fragment_item is not None
          assert isinstance(fragment_item, list)
          item_type = fragment_item[0]
        assert ex_nt_depth is None or grm_nt_depth >= ex_nt_depth
        if ex_nt_depth is not None and grm_nt_depth == ex_nt_depth and item_type is not None:
          if (item_type.startswith('"_str') or item_type == 'str'):
            assert fragment_item[1][0] == '"' and fragment_item[1][-1] == '"'
            fragment_str = json.loads(fragment_item[1])
            if fragment_str == prod["value"]:
              self._add_match_str_tail(
                cur_loop_det_list,  # loop_det_list
                par_node_id,  # par_node_id
                fragment_str,  # str_value
                ex_nt_depth,  # ex_nt_depth
                ex_id,  # ex_id
                expan_fragment,  # expan_fragment
                fragment_idx,  # cur_fragment_idx
                next_ex_contin,  # next_ex_contin
                is_immediate,  # is_immediate
                next_grm_contin  # next_grm_contin
              )
            else:
              if self._VERBOSE > 0: print()
              self._set_grm_back_tracking(grm_nt_depth, f"# STRING not matching (depth: {grm_nt_depth}={ex_nt_depth}). expansion: {fragment_str} grammar: {prod['value']}  BACKTRACKING..." if self._VERBOSE > -1 else None)
          elif item_type == 'nostr':
            if self._VERBOSE > 0: print()
            self._set_grm_back_tracking(grm_nt_depth, f"# STRING meets ##nostr##: {grm_nt_depth}={ex_nt_depth}). BACKTRACKING..." if self._VERBOSE > -1 else None)
          else:
            self._add_str_tail(
              cur_loop_det_list,  # loop_det_list
              par_node_id,  # par_node_id
              prod["value"],  # t_value
              cur_ex_contin,  # ex_cont
              is_immediate,  # is_immediate
              next_grm_contin  # next_grm_cont
            )
        else:
          self._add_str_tail(
            cur_loop_det_list,  # loop_det_list
            par_node_id,  # par_node_id
            prod["value"],  # t_value
            cur_ex_contin,  # ex_cont
            is_immediate,  # is_immediate
            next_grm_contin  # next_grm_cont
          )

      # prod_type case 10
      elif prod_type == "PATTERN" or prod_type == "TOKEN" or prod_type == "IMMEDIATE_TOKEN":
        is_immediate = prod_type == "IMMEDIATE_TOKEN"
        if cur_ex_contin is None:
          # CHECK cur_ex_contin. if cur_ex_contin is None, there's no value. No fragment item.
          assert fragment_item is None
          self._set_grm_back_tracking(grm_nt_depth, "PATTERN/TOKEN/IMMEDIATE_TOKEN fragment_item is None.")
          continue
        # check if it is immediate STRING. Hack to Hack. Not general case! If so, inline this prod.
        if is_immediate and prod["content"]["type"] == "STRING":
          self._inlined_prod_tail(
            cur_loop_det_list,  # loop_det_list
            cur_ex_contin,  # expan_continuation
            grm_nt_depth,  # grm_nt_depth
            par_node_id,  # par_node_id
            prod["content"],  # real_prod
            next_grm_contin  # next_grm_continuation
          )
        else:
          assert fragment_item[0].startswith('"_val') or fragment_item[0] == 'val'
          token_val = fragment_item[1]
          self._add_match_val_tail(
            cur_loop_det_list,  # loop_det_list
            ex_nt_depth,  # ex_nt_depth
            ex_id,  # ex_id
            expan_fragment,  # par_expan_fragment
            fragment_idx,  # elem_frag_idx
            next_ex_contin,  # next_expan_contin
            par_node_id,  # par_node_id
            token_val,  # t_value
            is_immediate,  # is_immediate
            next_grm_contin  # next_grm_cont
          )

      # prod_type case 11
      elif prod_type == "BLANK":
        if self._VERBOSE > 0: print("# match BLANK.")
        self._just_tail_call(
          cur_loop_det_list,  # loop_det_list
          cur_ex_contin,  # ex_cont
          next_grm_contin  # grm_cont
        )

      # prod_type case 12
      else:
        print("# Not supported prod type:", prod_type)
        assert False

  def get_current_elem_list(self):
    all_elem_nodes = _tail_stack_to_elem_list(self._tail_stack)
    return all_elem_nodes

  def get_elem_list_by_ids(self, ids):
    all_elem_nodes = [self._elem_dict[x] for x in ids]
    return all_elem_nodes

# end of class `DelimitedParser`

########################################## utils ##########################################

def _tail_stack_to_elem_list(tailstack):
  all_elem_nodes = [x[0] for x in tailstack if x[0] is not None]
  return all_elem_nodes

def _tail_stack_length_to_elem_list(info):
  tailstack, length = info
  all_elem_nodes = [x[0] for x in tailstack[:length] if x[0] is not None]
  return all_elem_nodes
