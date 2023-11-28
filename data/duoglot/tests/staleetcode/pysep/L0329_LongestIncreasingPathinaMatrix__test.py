from L0329_LongestIncreasingPathinaMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]]
    # output: 4
    # EXPLANATION:  The longest increasing path is <code>[1, 2, 6, 9]</code>.
    ,
    # example 2
    [[[3, 4, 5], [3, 2, 6], [2, 2, 1]]]
    # output: 4
    # EXPLANATION: The longest increasing path is <code>[3, 4, 5, 6]</code>. Moving diagonally is not allowed.
    ,
    # example 3
    [[[1]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
