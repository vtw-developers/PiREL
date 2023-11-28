from L0417_PacificAtlanticWaterFlow import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]]
    # output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    ,
    # example 2
    [[[2, 1], [1, 2]]]
    # output: [[0,0],[0,1],[1,0],[1,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
