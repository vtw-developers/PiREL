from L0074_Searcha2DMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3]
    # output: true
    ,
    # example 2
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
