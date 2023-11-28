from L1614_MaximumNestingDepthoftheParentheses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(1+(2*3)+((8)/4))+1"]
    # output: 3
    # EXPLANATION:  Digit 8 is inside of 3 nested parentheses in the string.
    ,
    # example 2
    ["(1)+((2))+(((3)))"]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
