from L1856_MaximumSubarrayMinProduct import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 2]]
    # output: 14
    # EXPLANATION:  The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2). 2 * (2+3+2) = 2 * 7 = 14.
    ,
    # example 2
    [[2, 3, 3, 1, 2]]
    # output: 18
    # EXPLANATION:  The maximum min-product is achieved with the subarray [3,3] (minimum value is 3). 3 * (3+3) = 3 * 6 = 18.
    ,
    # example 3
    [[3, 1, 5, 6, 4, 2]]
    # output: 60
    # EXPLANATION:  The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4). 4 * (5+6+4) = 4 * 15 = 60.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
