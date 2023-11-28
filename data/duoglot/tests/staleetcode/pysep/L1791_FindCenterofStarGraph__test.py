from L1791_FindCenterofStarGraph import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [4, 2]]]
    # output: 2
    # EXPLANATION:  As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
    ,
    # example 2
    [[[1, 2], [5, 1], [1, 3], [1, 4]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
