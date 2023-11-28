from L1391_CheckifThereisaValidPathinaGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 4, 3], [6, 5, 2]]]
    # output: true
    # EXPLANATION:  As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
    ,
    # example 2
    [[[1, 2, 1], [1, 2, 1]]]
    # output: false
    # EXPLANATION:  As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
    ,
    # example 3
    [[[1, 1, 2]]]
    # output: false
    # EXPLANATION:  You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
