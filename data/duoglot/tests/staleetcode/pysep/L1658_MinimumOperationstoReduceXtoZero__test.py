from L1658_MinimumOperationstoReduceXtoZero import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 4, 2, 3], 5]
    # output: 2
    # EXPLANATION:  The optimal solution is to remove the last two elements to reduce x to zero.
    ,
    # example 2
    [[5, 6, 7, 8, 9], 4]
    # output: -1
    ,
    # example 3
    [[3, 2, 20, 1, 1, 3], 10]
    # output: 5
    # EXPLANATION:  The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
