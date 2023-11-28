from L0785_IsGraphBipartite import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]]
    # output: false
    # EXPLANATION:  There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
    ,
    # example 2
    [[[1, 3], [0, 2], [1, 3], [0, 2]]]
    # output: true
    # EXPLANATION:  We can partition the nodes into two sets: {0, 2} and {1, 3}.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
