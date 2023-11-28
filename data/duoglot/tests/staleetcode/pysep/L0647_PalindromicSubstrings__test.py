from L0647_PalindromicSubstrings import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abc"]
    # output: 3
    # EXPLANATION:  Three palindromic strings: "a", "b", "c".
    ,
    # example 2
    ["aaa"]
    # output: 6
    # EXPLANATION:  Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
