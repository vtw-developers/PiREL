from L1790_CheckifOneStringSwapCanMakeStringsEqual import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bank", "kanb"]
    # output: true
    # EXPLANATION:  For example, swap the first character with the last character of s2 to make "bank".
    ,
    # example 2
    ["attack", "defend"]
    # output: false
    # EXPLANATION:  It is impossible to make them equal with one string swap.
    ,
    # example 3
    ["kelb", "kelb"]
    # output: true
    # EXPLANATION:  The two strings are already equal, so no string swap operation is required.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
