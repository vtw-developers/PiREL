from L0827_MakingALargeIsland import f_gold

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
    # output: 3
    # EXPLANATION:  Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
    ,
    # example 2
    [[[1, 1], [1, 0]]]
    # output: 4
    # EXPLANATION: Change the 0 to 1 and make the island bigger, only one island with area = 4.
    ,
    # example 3
    [[[1, 1], [1, 1]]]
    # output: 4
    # EXPLANATION:  Can't change any 0 to 1, only one island with area = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
