from L0566_ReshapetheMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3, 4]], 1, 4]
    # output: [[1,2,3,4]]
    ,
    # example 2
    [[[1, 2], [3, 4]], 2, 4]
    # output: [[1,2],[3,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
