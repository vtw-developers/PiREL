from L0962_MaximumWidthRamp import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[6, 0, 8, 2, 1, 5]]
    # output: 4
    # EXPLANATION:  The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
    ,
    # example 2
    [[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]]
    # output: 7
    # EXPLANATION:  The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
