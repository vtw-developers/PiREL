from L1087_BraceExpansion import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["{a,b}c{d,e}f"]
    # output: ["acdf","acef","bcdf","bcef"]
    ,
    # example 2
    ["abcd"]
    # output: ["abcd"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
