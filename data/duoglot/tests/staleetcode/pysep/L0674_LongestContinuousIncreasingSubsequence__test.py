from L0674_LongestContinuousIncreasingSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 4, 7]]
    # output: 3
    # EXPLANATION:  The longest continuous increasing subsequence is [1,3,5] with length 3. Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element 4.
    ,
    # example 2
    [[2, 2, 2, 2, 2]]
    # output: 1
    # EXPLANATION:  The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly increasing.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
