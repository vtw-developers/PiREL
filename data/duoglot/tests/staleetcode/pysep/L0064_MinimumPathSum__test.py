from L0064_MinimumPathSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]]
    # output: 7
    # EXPLANATION:  Because the path 1   3   1   1   1 minimizes the sum.
    ,
    # example 2
    [[[1, 2, 3], [4, 5, 6]]]
    # output: 12
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
