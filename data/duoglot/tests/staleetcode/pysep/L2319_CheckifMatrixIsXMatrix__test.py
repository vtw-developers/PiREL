from L2319_CheckifMatrixIsXMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]]
    # output: true
    # EXPLANATION:  Refer to the diagram above.  An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0. Thus, grid is an X-Matrix.
    ,
    # example 2
    [[[5, 7, 0], [0, 3, 1], [0, 5, 0]]]
    # output: false
    # EXPLANATION:  Refer to the diagram above. An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0. Thus, grid is not an X-Matrix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
