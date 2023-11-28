from L0159_LongestSubstringwithAtMostTwoDistinctCharacters import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["eceba"]
    # output: 3
    # EXPLANATION:  The substring is "ece" which its length is 3.
    ,
    # example 2
    ["ccaabbb"]
    # output: 5
    # EXPLANATION:  The substring is "aabbb" which its length is 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
