from L0325_MaximumSizeSubarraySumEqualsk import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, -1, 5, -2, 3], 3]
    # output: 4
    # EXPLANATION:  The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    ,
    # example 2
    [[-2, -1, 2, 1], 1]
    # output: 2
    # EXPLANATION:  The subarray [-1, 2] sums to 1 and is the longest.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
