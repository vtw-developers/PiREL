from L2017_GridGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 5, 4], [1, 5, 1]]]
    # output: 4
    # EXPLANATION:  The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 0 + 4 + 0 = 4 points.
    ,
    # example 2
    [[[3, 3, 1], [8, 5, 2]]]
    # output: 4
    # EXPLANATION:  The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 3 + 1 + 0 = 4 points.
    ,
    # example 3
    [[[1, 3, 1, 15], [1, 3, 3, 1]]]
    # output: 7
    # EXPLANATION: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue. The cells visited by the first robot are set to 0. The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
