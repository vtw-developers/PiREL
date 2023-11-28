from L1190_ReverseSubstringsBetweenEachPairofParentheses import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(abcd)"]
    # output: "dcba"
    ,
    # example 2
    ["(u(love)i)"]
    # output: "iloveu"
    # EXPLANATION:  The substring "love" is reversed first, then the whole string is reversed.
    ,
    # example 3
    ["(ed(et(oc))el)"]
    # output: "leetcode"
    # EXPLANATION:  First, we reverse the substring "oc", then "etco", and finally, the whole string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
