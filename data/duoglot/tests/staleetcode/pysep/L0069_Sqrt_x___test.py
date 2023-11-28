from L0069_Sqrt_x_ import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 2
    ,
    # example 2
    [8]
    # output: 2
    # EXPLANATION:  The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
