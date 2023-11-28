from L0883_ProjectionAreaof3DShapes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3, 4]]]
    # output: 17
    # EXPLANATION:  Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
    ,
    # example 2
    [[[2]]]
    # output: 5
    ,
    # example 3
    [[[1, 0], [0, 2]]]
    # output: 8
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
