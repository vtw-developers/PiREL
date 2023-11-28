from L0010_RegularExpressionMatching import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aa", "a"]
    # output: false
    # EXPLANATION:  "a" does not match the entire string "aa".
    ,
    # example 2
    ["aa", "a*"]
    # output: true
    # EXPLANATION:  '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    ,
    # example 3
    ["ab", ".*"]
    # output: true
    # EXPLANATION:  ".*" means "zero or more (*) of any character (.)".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
