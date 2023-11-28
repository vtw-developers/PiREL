from L1319_NumberofOperationstoMakeNetworkConnected import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [[0, 1], [0, 2], [1, 2]]]
    # output: 1
    # EXPLANATION:  Remove cable between computer 1 and 2 and place between computers 1 and 3.
    ,
    # example 2
    [6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]]
    # output: 2
    ,
    # example 3
    [6, [[0, 1], [0, 2], [0, 3], [1, 2]]]
    # output: -1
    # EXPLANATION:  There are not enough cables.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
