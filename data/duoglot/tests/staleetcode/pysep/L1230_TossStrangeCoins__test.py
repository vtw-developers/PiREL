from L1230_TossStrangeCoins import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0.4], 1]
    # output: 0.40000
    ,
    # example 2
    [[0.5, 0.5, 0.5, 0.5, 0.5], 0]
    # output: 0.03125
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
