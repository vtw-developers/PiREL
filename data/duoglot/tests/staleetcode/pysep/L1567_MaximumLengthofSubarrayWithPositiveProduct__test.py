from L1567_MaximumLengthofSubarrayWithPositiveProduct import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, -2, -3, 4]]
    # output: 4
    # EXPLANATION:  The array nums already has a positive product of 24.
    ,
    # example 2
    [[0, 1, -2, -3, -4]]
    # output: 3
    # EXPLANATION:  The longest subarray with positive product is [1,-2,-3] which has a product of 6. Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
    ,
    # example 3
    [[-1, -2, -3, 0, 1]]
    # output: 2
    # EXPLANATION:  The longest subarray with positive product is [-1,-2] or [-2,-3].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
