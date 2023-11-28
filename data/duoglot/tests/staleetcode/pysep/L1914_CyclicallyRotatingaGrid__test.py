from L1914_CyclicallyRotatingaGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[40, 10], [30, 20]], 1]
    # output: [[10,20],[40,30]]
    # EXPLANATION:  The figures above represent the grid at every state.
    ,
    # example 2
    [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2]
    # output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
    # EXPLANATION:  The figures above represent the grid at every state.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
