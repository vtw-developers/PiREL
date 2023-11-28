from L0322_CoinChange import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 5], 11]
    # output: 3
    # EXPLANATION:  11 = 5 + 5 + 1
    ,
    # example 2
    [[2], 3]
    # output: -1
    ,
    # example 3
    [[1], 0]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
