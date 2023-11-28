from L1557_MinimumNumberofVerticestoReachAllNodes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]]
    # output: [0,3]
    # EXPLANATION: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
    ,
    # example 2
    [5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]]
    # output: [0,2,3]
    # EXPLANATION: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
