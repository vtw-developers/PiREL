from L0802_FindEventualSafeStates import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [5], [0], [5], [], []]]
    # output: [2,4,5,6]
    # EXPLANATION:  The given graph is shown above. Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them. Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
    ,
    # example 2
    [[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]]
    # output: [4]
    # EXPLANATION:  Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
