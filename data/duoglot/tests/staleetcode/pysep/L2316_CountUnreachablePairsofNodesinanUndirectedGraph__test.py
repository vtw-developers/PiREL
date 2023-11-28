from L2316_CountUnreachablePairsofNodesinanUndirectedGraph import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1], [0, 2], [1, 2]]]
    # output: 0
    # EXPLANATION:  There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
    ,
    # example 2
    [7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]]
    # output: 14
    # EXPLANATION:  There are 14 pairs of nodes that are unreachable from each other: [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]]. Therefore, we return 14.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
