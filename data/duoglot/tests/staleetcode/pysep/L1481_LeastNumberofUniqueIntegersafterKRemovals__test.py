from L1481_LeastNumberofUniqueIntegersafterKRemovals import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 5, 4], 1]
    # output: 1
    # EXPLANATION: : Remove the single 4, only 5 is left.
    ,
    # example 2
    [[4, 3, 1, 1, 3, 3, 2], 3]
    # output: 2
    # EXPLANATION: : Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
