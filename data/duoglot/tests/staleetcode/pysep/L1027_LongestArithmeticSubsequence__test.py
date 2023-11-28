from L1027_LongestArithmeticSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 6, 9, 12]]
    # output: 4
    # EXPLANATION:  The whole array is an arithmetic sequence with steps of length = 3.
    ,
    # example 2
    [[9, 4, 7, 2, 10]]
    # output: 3
    # EXPLANATION:  The longest arithmetic subsequence is [4,7,10].
    ,
    # example 3
    [[20, 1, 15, 3, 10, 5, 8]]
    # output: 4
    # EXPLANATION:  The longest arithmetic subsequence is [20,15,10,5].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
