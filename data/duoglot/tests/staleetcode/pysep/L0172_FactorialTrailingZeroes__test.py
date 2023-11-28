from L0172_FactorialTrailingZeroes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: 0
    # EXPLANATION:  3! = 6, no trailing zero.
    ,
    # example 2
    [5]
    # output: 1
    # EXPLANATION:  5! = 120, one trailing zero.
    ,
    # example 3
    [0]
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
