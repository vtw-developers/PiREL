import util_sexpr
import consts


def parse_analyze_rules(code_str, show_disable=False):
  # No longer using the old preprocessing code. Otherwise offset is wrong.
  # code_str = "\n".join([x for x in code_str.split("\n") if not x.strip().startswith(";") and not x.strip() == ""])
  expected_rule_count = len(("\n" + code_str).split("\n(match_expand")) + len(("\n" + code_str).split("\n(ext_match_expand")) - 2
  sexpr_list, sexpr_loc_list, err = util_sexpr.parse_sexpr_list(code_str)
  assert expected_rule_count == len(sexpr_list)

  if sexpr_list is None:
    print("parsing error:", err)
    assert False, "parsing error"

  expansion_programs = []
  for sexpr in sexpr_list:
    decl_name = sexpr[0]
    if decl_name == "match_expand":
      assert len(sexpr) == 3, "match_expand expected length 3"
      expansion_programs.append({
        "type": "match_expand",
        "match": sexpr[1],
        "expand": sexpr[2]
      })
    elif decl_name == "ext_match_expand":
      assert len(sexpr) == 4, "ext_match_expand expected length 4"
      assert sexpr[3][0] == "flags", "ext_match_expand should have flags"
      flags = {x:True for x in sexpr[3][1:]}
      if '"disabled"' not in flags or show_disable:
        expansion_programs.append({
          "type": "ext_match_expand",
          "match": sexpr[1],
          "expand": sexpr[2],
          "flags": flags
        })
      else:
        if consts.DEBUG_VERBOSE > 0: print("# _set_program_str skipping disabled rule.")
    else:
      print("Unknown declarator name:", decl_name)
      assert False, "Unknown declarator name"

  def _get_rule_summary(rule):
    rule_type = rule["type"]

    def _get_main_symbols(match_or_expand):
      maex_type = match_or_expand[0]
      if maex_type == "fragment":
        return [str(x) for x in match_or_expand[1:]]

    if rule_type == "match_expand" or rule_type == "ext_match_expand":
      match_symbols = _get_main_symbols(rule["match"])
      expand_symbols = _get_main_symbols(rule["expand"])
      return f"{' '.join(match_symbols)} => {' '.join(expand_symbols)}"
    else:
      print("# Unsupported rule_type:", rule_type)
      assert False, "rule_type_not_supported"

  rule_ids = list(range(len(expansion_programs)))
  dbg_info = {
    "rule_ids": rule_ids,
    "summary_dict": {i:_get_rule_summary(expansion_programs[i]) for i in rule_ids},
    "rule_loc_dict": {i:sexpr_loc_list[i+1][0] for i in rule_ids}
  }

  return expansion_programs, dbg_info
