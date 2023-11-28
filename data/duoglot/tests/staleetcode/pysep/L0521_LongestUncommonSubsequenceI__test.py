from L0521_LongestUncommonSubsequenceI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aba", "cdc"]
    # output: 3
    # EXPLANATION:  One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc". Note that "cdc" is also a longest uncommon subsequence.
    ,
    # example 2
    ["aaa", "bbb"]
    # output: 3
    # EXPLANATION:  The longest uncommon subsequences are "aaa" and "bbb".
    ,
    # example 3
    ["aaa", "aaa"]
    # output: -1
    # EXPLANATION:  Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
