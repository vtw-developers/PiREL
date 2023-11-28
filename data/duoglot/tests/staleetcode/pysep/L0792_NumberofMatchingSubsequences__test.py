from L0792_NumberofMatchingSubsequences import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcde", ["a", "bb", "acd", "ace"]]
    # output: 3
    # EXPLANATION:  There are three strings in words that are a subsequence of s: "a", "acd", "ace".
    ,
    # example 2
    ["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
