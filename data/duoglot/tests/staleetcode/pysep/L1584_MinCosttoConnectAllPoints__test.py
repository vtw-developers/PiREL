from L1584_MinCosttoConnectAllPoints import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]]
    # output: 20
    # EXPLANATION:   <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1584.Min%20Cost%20to%20Connect%20All%20Points/images/c.png" style="width: 214px; height: 268px;" /> We can connect the points as shown above to get the minimum cost of 20. Notice that there is a unique path between every pair of points.
    ,
    # example 2
    [[[3, 12], [-2, 5], [-4, 1]]]
    # output: 18
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
