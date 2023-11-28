from L1005_MaximizeSumOfArrayAfterKNegations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 3], 1]
    # output: 5
    # EXPLANATION:  Choose index 1 and nums becomes [4,-2,3].
    ,
    # example 2
    [[3, -1, 0, 2], 3]
    # output: 6
    # EXPLANATION:  Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
    ,
    # example 3
    [[2, -3, -1, 5, -4], 2]
    # output: 13
    # EXPLANATION:  Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
