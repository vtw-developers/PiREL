from L0994_RottingOranges import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]
    # output: 4
    ,
    # example 2
    [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]]
    # output: -1
    # EXPLANATION:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    ,
    # example 3
    [[[0, 2]]]
    # output: 0
    # EXPLANATION:  Since there are already no fresh oranges at minute 0, the answer is just 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
