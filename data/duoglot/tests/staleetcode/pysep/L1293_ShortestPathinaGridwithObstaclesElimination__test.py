from L1293_ShortestPathinaGridwithObstaclesElimination import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1]
    # output: 6
    # EXPLANATION:   The shortest path without eliminating any obstacle is 10. The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> <strong>(3,2)</strong> -> (4,2).
    ,
    # example 2
    [[[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1]
    # output: -1
    # EXPLANATION:  We need to eliminate at least two obstacles to find such a walk.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
