from L0673_NumberofLongestIncreasingSubsequence import f_gold

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
    # output: 2
    # EXPLANATION:  The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
    ,
    # example 2
    [[2, 2, 2, 2, 2]]
    # output: 5
    # EXPLANATION:  The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
