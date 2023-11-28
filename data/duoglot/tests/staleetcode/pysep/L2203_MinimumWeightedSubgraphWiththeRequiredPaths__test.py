from L2203_MinimumWeightedSubgraphWiththeRequiredPaths import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]], 0, 1, 5]
    # output: 9
    # EXPLANATION:  The above figure represents the input graph. The blue edges represent one of the subgraphs that yield the optimal answer. Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.
    ,
    # example 2
    [3, [[0, 1, 1], [2, 1, 1]], 0, 1, 2]
    # output: -1
    # EXPLANATION:  The above figure represents the input graph. It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
