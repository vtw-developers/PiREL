from L1143_LongestCommonSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcde", "ace"]
    # output: 3
    # EXPLANATION:  The longest common subsequence is "ace" and its length is 3.
    ,
    # example 2
    ["abc", "abc"]
    # output: 3
    # EXPLANATION:  The longest common subsequence is "abc" and its length is 3.
    ,
    # example 3
    ["abc", "def"]
    # output: 0
    # EXPLANATION:  There is no such common subsequence, so the result is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
