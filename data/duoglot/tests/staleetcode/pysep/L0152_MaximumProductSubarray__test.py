from L0152_MaximumProductSubarray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, -2, 4]]
    # output: 6
    # EXPLANATION:  [2,3] has the largest product 6.
    ,
    # example 2
    [[-2, 0, -1]]
    # output: 0
    # EXPLANATION:  The result cannot be 2, because [-2,-1] is not a subarray.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
