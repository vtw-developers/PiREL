from L1466_ReorderRoutestoMakeAllPathsLeadtotheCityZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]]
    # output: 3
    # EXPLANATION: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    ,
    # example 2
    [5, [[1, 0], [1, 2], [3, 2], [3, 4]]]
    # output: 2
    # EXPLANATION: Change the direction of edges show in red such that each node can reach the node 0 (capital).
    ,
    # example 3
    [3, [[1, 0], [2, 0]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
