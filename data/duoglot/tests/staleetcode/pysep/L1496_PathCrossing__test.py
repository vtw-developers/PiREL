from L1496_PathCrossing import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["NES"]
    # output: false
    # EXPLANATION:  Notice that the path doesn't cross any point more than once.
    ,
    # example 2
    ["NESWW"]
    # output: true
    # EXPLANATION:  Notice that the path visits the origin twice.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
