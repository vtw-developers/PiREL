import cython
import sys
if cython.compiled: print("[grammar] Compiled.", file=sys.stderr)
else: print("[grammar] Interpreted.", file=sys.stderr)
####################################

import util_traverse
import util_log
import json
import consts


DIRECT_CSET_KEY = "_direct_cset"
SYM_AHEADSET_KEY = "_sym_ahead_set"

GRM_VERBOSE = 0


def grm_prod_pretty(prod):
  prod_type = prod["type"]
  res = None
  if prod_type == "REPEAT":
    res = f"(REPEAT {grm_prod_pretty(prod['content'])})"
  elif prod_type == "REPEAT1":
    res = f"(REPEAT1 {grm_prod_pretty(prod['content'])})"
  elif prod_type == "SEQ":
    res = f"(SEQ {' '.join([grm_prod_pretty(x) for x in prod['members']])})"
  elif prod_type == "CHOICE":
    res = f"(CHOICE {' | '.join([grm_prod_pretty(x) for x in prod['members']])})"
  elif prod_type == "BLANK":
    res = "(BLANK)"
  elif prod_type == "SYMBOL":
    res = f"(SYMBOL {prod['name']})"
  elif prod_type == "FIELD":
    res = f"(FIELD {prod['name']} {grm_prod_pretty(prod['content'])})"
  elif prod_type == "STRING":
    res = f"(STR {prod['value']})"
  elif prod_type == "TOKEN":
    res = f"(TOKEN ...)"
  elif prod_type == "ALIAS":
    res = f"(ALIAS {prod['named']} {prod['value']} {grm_prod_pretty(prod['content'])})"
  elif prod_type == "PREC" or prod_type == "PREC_LEFT" or prod_type == "PREC_RIGHT" or prod_type == "PREC_DYNAMIC":
    res = f"({prod_type} {prod['value']} {grm_prod_pretty(prod['content'])})"
  else:
    res = str(prod)
  return res


def grm_get_prod(grammar, x):
  return grammar["rules"][x]


def grm_is_inlined_NT(grammar, x):
  return x in grammar["inline"]


def grm_is_supertype_NT(grammar, x):
  return x in grammar["supertypes"]


def grm_is_hidden_NT(grammar, x):
  return x.startswith("_")


def grm_is_skipped_NT(grammar, x):
  return \
    grm_is_inlined_NT(grammar, x) \
    or \
    grm_is_hidden_NT(grammar, x) \
    or \
    grm_is_supertype_NT(grammar, x)


def grm_is_external_NT(grammar, x):
  return x in grammar["_external_symbols"]


def grm_external_NT_pretty_string(grammar, external_state_id, external_NT):
  if consts.DEBUG_VERBOSE > -10: print("WARNING: grm_external_NT_pretty_string is not implemented. dumb value.")
  return 1, external_NT


def _grm_preprocess_hack_py(grammar):
  # hack for py
  print("# !!! Special hacks for python grammar. Add fake rules.")
  assert "string_content" not in grammar["rules"]
  grammar["rules"]["string_content"] = {
    "type": "IMMEDIATE_TOKEN",
    "content": {
      "type": "PATTERN",
      "is_fake": True
    },
    "is_fake": True
  }


def _grm_preprocess_hack_js(grammar):
  # hack for js
  print("# !!! Special hacks for javascript grammar. Add fake rules.")
  assert "template_chars" not in grammar["rules"]
  grammar["rules"]["template_chars"] = {
    "type": "IMMEDIATE_TOKEN",
    "content": {
      "type": "PATTERN",
      "is_fake": True
    },
    "is_fake": True
  }


# TODO what does this function do?
def grm_preprocess(lang_prefix, grammar):

  # 1 hack the grammars (language specific)
  if lang_prefix == "py":
    _grm_preprocess_hack_py(grammar)
  elif lang_prefix == "js":
    _grm_preprocess_hack_js(grammar)

  # 2 externals
  externals = [x["name"] for x in grammar["externals"]]
  grammar["_external_symbols"] = externals

  # 3 start rule and prefix
  grammar["_initial_prod"] = {
    "type": "SYMBOL",
    "name": grm_get_start_NT(grammar)
  }
  grammar["_prefix"] = lang_prefix

  print(f"\n# grm_preprocess {lang_prefix} _external_symbols:", externals)

  # 4 inner function 1
  def _transform_alias_subprod_rec_inner_fun(prod, aliased_name):
    '''change SYMBOL to SYMBOL_JUMP recursively for the entire `prod`'''
    prod_type = prod["type"]

    if prod_type == "SYMBOL":
      prod["type"] = "SYMBOL_JUMP"

    elif prod_type == "CHOICE":
      prod_members = prod["members"]
      for current_member in prod_members:
        _transform_alias_subprod_rec_inner_fun(current_member, aliased_name)

    elif prod_type == "PREC":
      _transform_alias_subprod_rec_inner_fun(prod["content"], aliased_name)

    elif prod_type == "PATTERN":
      return

    elif prod_type == "STRING":
      return

    else:
      print("ERROR. Not handled prod type in alias prod:", aliased_name, prod_type)
      assert "NOT_SUPPORTED_PROD_TYPE_IN_ALIAS" == 0

  all_aliased_symbols = set()

  # 5 inner function 2
  def _find_transform_aliases_inner_fun(key, node):
    '''transforms nodes with type `ALIAS`'''
    # dict where `type` is `ALIAS`
    if isinstance(node, dict) and "type" in node and node["type"] == "ALIAS":

      if node["named"] == False:
        strval = node["value"]
        node["pt_content"] = {
          "type": "STRING",
          "value": strval
        }
        return True, False  # skip, stop

      else:
        all_aliased_symbols.add(node["value"])
        _transform_alias_subprod_rec_inner_fun(node["content"], node["value"])
        return True, False  # skip, stop

    return False, False  # skip, stop

  util_traverse.traverse_nested_list_and_dict(grammar["rules"], _find_transform_aliases_inner_fun)

  # 6 inner function 3
  def _find_transform_immediate_string_inner_fun(key, node):

    if isinstance(node, dict) and "type" in node and node["type"] == "IMMEDIATE_TOKEN":

      if node["content"]["type"] == "STRING":
        node["content"]["immediate"] = True
        return True, False  # skip, stop
      else:
        return True, False  # skip, stop

    return False, False  # skip, stop

  util_traverse.traverse_nested_list_and_dict(grammar["rules"], _find_transform_immediate_string_inner_fun)

  grammar["_aliased_symbols"] = all_aliased_symbols
  print(f"# grm_preprocess {lang_prefix} _aliased_symbols:", all_aliased_symbols)
  # add _diret_cset to each prod

  # 7 inner function 4
  def _mark_get_possible_direct_children_rec_inner_fun(prod):

    if DIRECT_CSET_KEY in prod:
      return prod[DIRECT_CSET_KEY]

    cset = set()
    prod_type = prod["type"]

    if prod_type == "SEQ" or prod_type == "CHOICE":
      prod_members = prod["members"]
      for current_member in prod_members:
        member_set = _mark_get_possible_direct_children_rec_inner_fun(current_member)
        cset.update(member_set)

    elif prod_type == "REPEAT" or prod_type == "REPEAT1" or prod_type == "FIELD" \
      or prod_type == "PREC_DYNAMIC" or prod_type == "PREC" \
      or prod_type == "PREC_LEFT" or prod_type == "PREC_RIGHT":
      content_set = _mark_get_possible_direct_children_rec_inner_fun(prod["content"])
      cset.update(content_set)

    elif prod_type == "STRING":
      cset.add(("str", json.dumps(prod["value"])))

    elif prod_type == "SYMBOL":
      symbol_name = prod["name"]
      if grm_is_skipped_NT(grammar, symbol_name):
        if grm_is_external_NT(grammar, symbol_name):
          cset.add(("ext", f'"{symbol_name}"'))
        else:
          real_prod = grm_get_prod(grammar, symbol_name)
          real_set = _mark_get_possible_direct_children_rec_inner_fun(real_prod)
          cset.update(real_set)
      else: # notice that symbol/alias_symbol currently is not checked in dlmparser
        cset.add(("symbol", f'"{symbol_name}"'))

    elif prod_type == "BLANK":
      cset.add(("blank", None))

    elif prod_type == "TOKEN" or prod_type == "IMMEDIATE_TOKEN":
      cset.add(("token", None))

    elif prod_type == "PATTERN":
      cset.add(("pattern", None))

    elif prod_type == "ALIAS":
      if prod["named"] == False:
        cset.add(("str", json.dumps(prod["value"]))) # Just treat it as str in pt.
      else:
        alias_symbol = prod["value"]
        if grm_is_skipped_NT(grammar, alias_symbol):
          # the aliased symbol is inlined or supertype. go to real prod.
          real_prod = prod["content"]
          real_set = _mark_get_possible_direct_children_rec_inner_fun(real_prod)
          cset.update(real_set)
        else: # notice that symbol/alias_symbol currently is not checked in dlmparser
          cset.add(("alias_symbol", f'"{alias_symbol}"'))

    else:
      print("# ERROR: Unknown prod type:", prod_type)
      assert 0 == "Preprocessing: Unknown prod type"

    prod[DIRECT_CSET_KEY] = cset
    return cset

  # 8 process each prod
  print(f"# add {DIRECT_CSET_KEY} to each prod...")
  for prod_key in grammar["rules"]:
    prod = grammar["rules"][prod_key]
    cset = _mark_get_possible_direct_children_rec_inner_fun(prod)

  # 9 add _diret_cset to each prod, inner function 5
  def _update_get_possible_ahead_rec_inner_fun(prod, ahead):
    _contains = lambda big, small : len(small - big) == 0
    ahead_len = len(ahead)
    assert DIRECT_CSET_KEY in prod
    this_cset = prod[DIRECT_CSET_KEY]
    # this is only set once (except for REPEAT)
    # assert SYM_AHEADSET_KEY not in prod
    min_ahead_set = this_cset.union(ahead)
    new_ahead_set = None
    # processing
    prod_type = prod["type"]
    if prod_type == "SEQ":
      prod_members = prod["members"]
      current_ahead = ahead
      for idx in range(len(prod_members)-1, -1, -1):
        focus_member = prod_members[idx]
        current_ahead = _update_get_possible_ahead_rec_inner_fun(focus_member, current_ahead)
        assert ahead_len == len(ahead)
      new_ahead_set = current_ahead
    elif prod_type == "CHOICE":
      prod_members = prod["members"]
      union_ahead = set()
      for idx in range(len(prod_members)-1, -1, -1):
        focus_member = prod_members[idx]
        member_ahead = _update_get_possible_ahead_rec_inner_fun(focus_member, ahead)
        assert ahead_len == len(ahead)
        union_ahead.update(member_ahead)
      new_ahead_set = union_ahead
    elif prod_type == "REPEAT" or prod_type == "REPEAT1":
      content_prod = prod["content"]
      content_ahead1 = _update_get_possible_ahead_rec_inner_fun(content_prod, ahead)
      content_ahead2 = _update_get_possible_ahead_rec_inner_fun(content_prod, content_ahead1)
      new_ahead_set = content_ahead2
    elif prod_type == "FIELD" \
      or prod_type == "PREC_DYNAMIC" or prod_type == "PREC" \
      or prod_type == "PREC_LEFT" or prod_type == "PREC_RIGHT":
      content_prod = prod["content"]
      content_ahead = _update_get_possible_ahead_rec_inner_fun(content_prod, ahead)
      new_ahead_set = content_ahead
    elif prod_type == "STRING" or prod_type == "BLANK" \
      or prod_type == "TOKEN" or prod_type == "IMMEDIATE_TOKEN" or prod_type == "PATTERN":
      new_ahead_set = min_ahead_set
    elif prod_type == "SYMBOL":
      symbol_name = prod["name"]
      if grm_is_skipped_NT(grammar, symbol_name):
        if grm_is_external_NT(grammar, symbol_name):
          new_ahead_set = min_ahead_set
        else:
          real_prod = grm_get_prod(grammar, symbol_name)
          real_cset = real_prod[DIRECT_CSET_KEY]
          new_ahead_set = ahead.union(real_cset)
      else:
        new_ahead_set = min_ahead_set
    elif prod_type == "ALIAS":
      if prod["named"] == False:
        new_ahead_set = min_ahead_set
      else:
        alias_symbol = prod["value"]
        if grm_is_skipped_NT(grammar, alias_symbol):
          # the aliased symbol is inlined or supertype. go to real prod.
          real_prod = prod["content"]
          real_ahead = _update_get_possible_ahead_rec_inner_fun(real_prod, ahead)
          new_ahead_set = real_ahead
        else:
          new_ahead_set = min_ahead_set
    else:
      print("# ERROR: _update_get_possible_ahead_rec_inner_fun Unknown prod type:", prod_type)
      assert 0 == "Preprocessing: Unknown prod type"
    if not _contains(new_ahead_set, min_ahead_set):
      print("# ERROR: _update_get_possible_ahead_rec_inner_fun contains assertion failed:\n  new_ahead_set:",
        new_ahead_set, "\n  min_ahead_set:", min_ahead_set, "\n  b - a:", min_ahead_set - new_ahead_set)
      assert 0 == "contains assertion failed"
    prod[SYM_AHEADSET_KEY] = new_ahead_set
    return new_ahead_set

  # 10 process each prod
  print(f"# add {SYM_AHEADSET_KEY} to each prod...")
  empty_set = set()

  for prod_key in grammar["rules"]:
    if not grm_is_skipped_NT(grammar, prod_key):
      prod = grammar["rules"][prod_key]
      _update_get_possible_ahead_rec_inner_fun(prod, empty_set)
      assert len(empty_set) == 0

  for prod_key in grammar["rules"]:
    if grm_is_skipped_NT(grammar, prod_key):
      prod = grammar["rules"][prod_key]
      assert SYM_AHEADSET_KEY not in prod

  # 11 debug print, inner function 6
  def _dbg_print_choice_aheads_inner_fun(key, prod_node):

    if isinstance(prod_node, set):
      return True, False  # skip, stop

    if isinstance(prod_node, str) or isinstance(prod_node, int):
      return True, False  # skip, stop

    if isinstance(key, int):
      return True, False  # skip, stop

    if isinstance(key, str) and key.find("binary") < 0:
      return False, False  # skip, stop

    if isinstance(prod_node, dict):
      if prod_node["type"] == "CHOICE":
        ahead = prod_node[SYM_AHEADSET_KEY]
        print(f"---------------- {key} CHOICE:", len(prod_node["members"]), " ahead_size:", len(ahead), "-------------")

        for member in prod_node["members"]:
          member_cset = member[DIRECT_CSET_KEY]
          member_ahead = member[SYM_AHEADSET_KEY]
          print("  MEMBER:", grm_prod_pretty(member),
                "\n    -----cset: ", len(member_cset), member_cset,
                "\n    -----ahead: ", len(member_ahead), member_ahead)

    return False, False  # skip, stop

  if GRM_VERBOSE > 0: util_traverse.traverse_nested_list_and_dict(grammar["rules"], _dbg_print_choice_aheads_inner_fun)

  # 12 file logging for debugging
  util_log.log_json(lang_prefix + "_" + "grammar", grammar)


def grm_get_start_NT(grammar):
  start_NT = list(dict.keys(grammar["rules"]))[0]
  print("# grm_get_start_NT:", start_NT)
  return start_NT


def grm_get_all_NTs(grammar):
  all_NTs = []
  for key in grammar["rules"]:
    all_NTs.append(key)
  return all_NTs


def grm_get_all_inlined_NTs(grammar):
  all_inlined_NTs = []
  for key in grammar["inline"]:
    all_inlined_NTs.append(key)
  return all_inlined_NTs


def grm_get_all_not_inlined_NTs(grammar):
  all_NTs = grm_get_all_NTs(grammar)
  all_inlined_NTs = grm_get_all_inlined_NTs(grammar)
  all_not_inlined_NTs = [x for x in all_NTs if x not in all_inlined_NTs]
  return all_not_inlined_NTs
