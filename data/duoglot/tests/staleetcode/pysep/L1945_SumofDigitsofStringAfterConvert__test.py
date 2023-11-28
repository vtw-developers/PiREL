from L1945_SumofDigitsofStringAfterConvert import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["iiii", 1]
    # output: 36
    # EXPLANATION:  The operations are as follows: - Convert: "iiii"   "(9)(9)(9)(9)"   "9999"   9999 - Transform #1: 9999   9 + 9 + 9 + 9   36 Thus the resulting integer is 36.
    ,
    # example 2
    ["leetcode", 2]
    # output: 6
    # EXPLANATION:  The operations are as follows: - Convert: "leetcode"   "(12)(5)(5)(20)(3)(15)(4)(5)"   "12552031545"   12552031545 - Transform #1: 12552031545   1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5   33 - Transform #2: 33   3 + 3   6 Thus the resulting integer is 6.
    ,
    # example 3
    ["zbax", 2]
    # output: 8
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
