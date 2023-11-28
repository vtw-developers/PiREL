from L0005_LongestPalindromicSubstring import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["babad"]
    # output: "bab"
    # EXPLANATION:  "aba" is also a valid answer.
    ,
    # example 2
    ["cbbd"]
    # output: "bb"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
