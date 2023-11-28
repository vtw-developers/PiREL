from L2059_MinimumOperationstoConvertNumber import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 12], 2, 12]
    # output: 2
    # EXPLANATION:  We can go from 2   14   12 with the following 2 operations. - 2 + 12 = 14 - 14 - 2 = 12
    ,
    # example 2
    [[3, 5, 7], 0, -4]
    # output: 2
    # EXPLANATION:  We can go from 0   3   -4 with the following 2 operations.  - 0 + 3 = 3 - 3 - 7 = -4 Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
    ,
    # example 3
    [[2, 8, 16], 0, 1]
    # output: -1
    # EXPLANATION:  There is no way to convert 0 into 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
