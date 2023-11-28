from L1020_NumberofEnclaves import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]]
    # output: 3
    # EXPLANATION:  There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
    ,
    # example 2
    [[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]]
    # output: 0
    # EXPLANATION:  All 1s are either on the boundary or can reach the boundary.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
