import re
import pyparsing as pp


# https://gist.github.com/hastern/ac2d7eab7a2a85f588d1
# S-expression grammar
LP = pp.Literal("(").suppress()
RP = pp.Literal(")").suppress()
String = pp.Word(pp.alphanums + '_')
SingleQuoteString = pp.QuotedString(quoteChar="'", esc_char="\\", esc_quote="\\'", unquoteResults=False)
DoubleQuoteString = pp.QuotedString(quoteChar='"', esc_char="\\", esc_quote='\\"', unquoteResults=False)
QuotedString = SingleQuoteString | DoubleQuoteString
Atom = String | QuotedString
Comment = (pp.Literal(";") + pp.restOfLine()).suppress().ignore(QuotedString)
SExpr = pp.Forward()
SExprList = pp.Group(pp.Located(pp.ZeroOrMore(SExpr | Atom | Comment))) # replace pp.Group by pp.Located
SExpr << LP + SExprList + RP


def parse_sexpr_list(sexprlist_str):
  try:
    pr = SExprList.parseString(sexprlist_str)
    pr_list = pr[0].as_list()
    # print(pr_list)
    def _get_expr_list(pr_list):
      if not isinstance(pr_list, list): return pr_list
      assert len(pr_list) == 3
      return [_get_expr_list(x) for x in pr_list[1]]
    def _get_loc_list(pr_list):
      if not isinstance(pr_list, list): return pr_list
      assert len(pr_list) == 3
      return [(pr_list[0], pr_list[2])] + [_get_loc_list(x) for x in pr_list[1]]
    return _get_expr_list(pr_list), _get_loc_list(pr_list), None
  except pp.ParseException as e:
    return None, None, e


if __name__ == "__main__":
  print("test sexpr list parse.")

  def test_str(s):
    print("------- test_str -------")
    print(s)
    result, loc, err = parse_sexpr_list(s)
    if result is not None:
      print(result)
      print(loc)
    else:
      print("--- error ---")
      print(err)

  test_str("""(a (b "hello")) (c)""")
  test_str("""(a (b "hello"))
(c)""")
  test_str("""
(a (b "hello"))
; what's this?
(c)
""")
  test_str("""
(a (b "hello")) ; what's (a and b)?
; what's this?
(c) ; what's (c and d)?
""")
  test_str("""(a "\\"\\"\\"") (c)""")
