from L0343_IntegerBreak import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 1
    # EXPLANATION:  2 = 1 + 1, 1   1 = 1.
    ,
    # example 2
    [10]
    # output: 36
    # EXPLANATION:  10 = 3 + 3 + 4, 3   3   4 = 36.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
