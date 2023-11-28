from L0516_LongestPalindromicSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bbbab"]
    # output: 4
    # EXPLANATION:  One possible longest palindromic subsequence is "bbbb".
    ,
    # example 2
    ["cbbd"]
    # output: 2
    # EXPLANATION:  One possible longest palindromic subsequence is "bb".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
