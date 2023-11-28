from L0029_DivideTwoIntegers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10, 3]
    # output: 3
    # EXPLANATION:  10/3 = 3.33333.. which is truncated to 3.
    ,
    # example 2
    [7, -3]
    # output: -2
    # EXPLANATION:  7/-3 = -2.33333.. which is truncated to -2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
