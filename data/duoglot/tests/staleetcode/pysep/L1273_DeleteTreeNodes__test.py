from L1273_DeleteTreeNodes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1]]
    # output: 2
    ,
    # example 2
    [7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2]]
    # output: 6
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
