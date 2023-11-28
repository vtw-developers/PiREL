from L1961_CheckIfStringIsaPrefixofArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["iloveleetcode", ["i", "love", "leetcode", "apples"]]
    # output: true
    # EXPLANATION:  s can be made by concatenating "i", "love", and "leetcode" together.
    ,
    # example 2
    ["iloveleetcode", ["apples", "i", "love", "leetcode"]]
    # output: false
    # EXPLANATION:  It is impossible to make s using a prefix of arr.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
