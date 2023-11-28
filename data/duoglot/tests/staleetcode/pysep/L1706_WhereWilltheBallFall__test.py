from L1706_WhereWilltheBallFall import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]]
    # output: [1,-1,-1,-1,-1]
    # EXPLANATION:  This example is shown in the photo. Ball b0 is dropped at column 0 and falls out of the box at column 1. Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1. Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0. Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0. Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
    ,
    # example 2
    [[[-1]]]
    # output: [-1]
    # EXPLANATION:  The ball gets stuck against the left wall.
    ,
    # example 3
    [[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]]
    # output: [0,1,2,3,4,-1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
