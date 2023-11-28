from L1234_ReplacetheSubstringforBalancedString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["QWER"]
    # output: 0
    # EXPLANATION:  s is already balanced.
    ,
    # example 2
    ["QQWE"]
    # output: 1
    # EXPLANATION:  We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
    ,
    # example 3
    ["QQQW"]
    # output: 2
    # EXPLANATION:  We can replace the first "QQ" to "ER".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
