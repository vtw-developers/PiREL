from L1102_PathWithMaximumMinimumValue import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[5, 4, 5], [1, 2, 6], [7, 4, 6]]]
    # output: 4
    # EXPLANATION:  The path with the maximum score is highlighted in yellow.
    ,
    # example 2
    [[[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]]
    # output: 2
    ,
    # example 3
    [[[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]]
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
