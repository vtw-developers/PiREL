from L0518_CoinChange2 import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [1, 2, 5]]
    # output: 4
    # EXPLANATION:  there are four ways to make up the amount: 5=5 5=2+2+1 5=2+1+1+1 5=1+1+1+1+1
    ,
    # example 2
    [3, [2]]
    # output: 0
    # EXPLANATION:  the amount of 3 cannot be made up just with coins of 2.
    ,
    # example 3
    [10, [10]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
