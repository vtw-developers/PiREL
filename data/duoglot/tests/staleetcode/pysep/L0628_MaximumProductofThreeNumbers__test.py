from L0628_MaximumProductofThreeNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 6
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: 24
    ,
    # example 3
    [[-1, -2, -3]]
    # output: -6
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
