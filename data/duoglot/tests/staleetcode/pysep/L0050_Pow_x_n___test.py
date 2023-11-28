from L0050_Pow_x_n_ import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2.0, 10]
    # output: 1024.00000
    ,
    # example 2
    [2.1, 3]
    # output: 9.26100
    ,
    # example 3
    [2.0, -2]
    # output: 0.25000
    # EXPLANATION:  2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
