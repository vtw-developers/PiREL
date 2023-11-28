from L0907_SumofSubarrayMinimums import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 4]]
    # output: 17
    # EXPLANATION:   Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].  Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum is 17.
    ,
    # example 2
    [[11, 81, 94, 43, 3]]
    # output: 444
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
