from L1800_MaximumAscendingSubarraySum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 20, 30, 5, 10, 50]]
    # output: 65
    # EXPLANATION: [5,10,50] is the ascending subarray with the maximum sum of 65.
    ,
    # example 2
    [[10, 20, 30, 40, 50]]
    # output: 150
    # EXPLANATION: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
    ,
    # example 3
    [[12, 17, 15, 13, 10, 11, 12]]
    # output: 33
    # EXPLANATION: [10,11,12] is the ascending subarray with the maximum sum of 33.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
