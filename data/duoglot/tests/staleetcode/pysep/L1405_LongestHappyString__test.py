from L1405_LongestHappyString import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 1, 7]
    # output: "ccaccbcc"
    # EXPLANATION:  "ccbccacc" would also be a correct answer.
    ,
    # example 2
    [7, 1, 0]
    # output: "aabaa"
    # EXPLANATION:  It is the only correct answer in this case.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
