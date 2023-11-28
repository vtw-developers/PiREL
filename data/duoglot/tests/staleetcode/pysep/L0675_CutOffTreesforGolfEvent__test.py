from L0675_CutOffTreesforGolfEvent import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [0, 0, 4], [7, 6, 5]]]
    # output: 6
    # EXPLANATION:  Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.
    ,
    # example 2
    [[[1, 2, 3], [0, 0, 0], [7, 6, 5]]]
    # output: -1
    # EXPLANATION:  The trees in the bottom row cannot be accessed as the middle row is blocked.
    ,
    # example 3
    [[[2, 3, 4], [0, 0, 5], [8, 7, 6]]]
    # output: 6
    # EXPLANATION:  You can follow the same path as Example 1 to cut off all the trees. Note that you can cut off the first tree at (0, 0) before making any steps.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
