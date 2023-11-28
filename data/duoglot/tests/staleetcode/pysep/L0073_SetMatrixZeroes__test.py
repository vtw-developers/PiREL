from L0073_SetMatrixZeroes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: [[1,0,1],[0,0,0],[1,0,1]]
    ,
    # example 2
    [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]]
    # output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
