from L1631_PathWithMinimumEffort import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]]
    # output: 2
    # EXPLANATION:  The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.  This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
    ,
    # example 2
    [[[1, 2, 3], [3, 8, 4], [5, 3, 5]]]
    # output: 1
    # EXPLANATION:  The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
    ,
    # example 3
    [[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]]
    # output: 0
    # EXPLANATION:  This route does not require any effort.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
