from L0704_BinarySearch import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 0, 3, 5, 9, 12], 9]
    # output: 4
    # EXPLANATION:  9 exists in nums and its index is 4
    ,
    # example 2
    [[-1, 0, 3, 5, 9, 12], 2]
    # output: -1
    # EXPLANATION:  2 does not exist in nums so return -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
