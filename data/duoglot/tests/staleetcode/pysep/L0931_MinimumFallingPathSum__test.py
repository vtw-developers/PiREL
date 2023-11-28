from L0931_MinimumFallingPathSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 3], [6, 5, 4], [7, 8, 9]]]
    # output: 13
    # EXPLANATION:  There are two falling paths with a minimum sum as shown.
    ,
    # example 2
    [[[-19, 57], [-40, -5]]]
    # output: -59
    # EXPLANATION:  The falling path with a minimum sum is shown.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
