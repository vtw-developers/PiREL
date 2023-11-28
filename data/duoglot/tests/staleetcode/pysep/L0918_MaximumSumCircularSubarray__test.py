from L0918_MaximumSumCircularSubarray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, -2, 3, -2]]
    # output: 3
    # EXPLANATION:  Subarray [3] has maximum sum 3.
    ,
    # example 2
    [[5, -3, 5]]
    # output: 10
    # EXPLANATION:  Subarray [5,5] has maximum sum 5 + 5 = 10.
    ,
    # example 3
    [[-3, -2, -3]]
    # output: -2
    # EXPLANATION:  Subarray [-2] has maximum sum -2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
