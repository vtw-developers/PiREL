from L0410_SplitArrayLargestSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 2, 5, 10, 8], 2]
    # output: 18
    # EXPLANATION:  There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
    ,
    # example 2
    [[1, 2, 3, 4, 5], 2]
    # output: 9
    ,
    # example 3
    [[1, 4, 4], 3]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
