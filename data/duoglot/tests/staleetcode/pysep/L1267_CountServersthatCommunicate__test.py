from L1267_CountServersthatCommunicate import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0], [0, 1]]]
    # output: 0
    # EXPLANATION:  No servers can communicate with others.
    ,
    # example 2
    [[[1, 0], [1, 1]]]
    # output: 3
    # EXPLANATION:  All three servers can communicate with at least one other server.
    ,
    # example 3
    [[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]
    # output: 4
    # EXPLANATION:  The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
