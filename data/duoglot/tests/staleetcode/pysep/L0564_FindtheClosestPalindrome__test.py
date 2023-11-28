from L0564_FindtheClosestPalindrome import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["123"]
    # output: "121"
    ,
    # example 2
    ["1"]
    # output: "0"
    # EXPLANATION:  0 and 2 are the closest palindromes but we return the smallest which is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
