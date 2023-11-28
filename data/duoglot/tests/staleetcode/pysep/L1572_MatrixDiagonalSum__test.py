from L1572_MatrixDiagonalSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: 25
    # EXPLANATION: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25 Notice that element mat[1][1] = 5 is counted only once.
    ,
    # example 2
    [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]
    # output: 8
    ,
    # example 3
    [[[5]]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
