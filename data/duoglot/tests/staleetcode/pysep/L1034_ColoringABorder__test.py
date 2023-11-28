from L1034_ColoringABorder import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [1, 2]], 0, 0, 3]
    # output: [[3,3],[3,2]]
    ,
    # example 2
    [[[1, 2, 2], [2, 3, 2]], 0, 1, 3]
    # output: [[1,3,3],[2,3,3]]
    ,
    # example 3
    [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2]
    # output: [[2,2,2],[2,1,2],[2,2,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
