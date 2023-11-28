from L2045_SecondMinimumTimetoReachDestination import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5]
    # output: 13
    # EXPLANATION:  The figure on the left shows the given graph. The blue path in the figure on the right is the minimum time path. The time taken is: - Start at 1, time elapsed=0 - 1 -> 4: 3 minutes, time elapsed=3 - 4 -> 5: 3 minutes, time elapsed=6 Hence the minimum time needed is 6 minutes.  The red path shows the path to get the second minimum time.  -   Start at 1, time elapsed=0 -   1 -> 3: 3 minutes, time elapsed=3 -   3 -> 4: 3 minutes, time elapsed=6 -   Wait at 4 for 4 minutes, time elapsed=10 -   4 -> 5: 3 minutes, time elapsed=13 Hence the second minimum time is 13 minutes.
    ,
    # example 2
    [2, [[1, 2]], 3, 2]
    # output: 11
    # EXPLANATION:  The minimum time path is 1 -> 2 with time = 3 minutes. The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
