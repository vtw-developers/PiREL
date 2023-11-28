from L0084_LargestRectangleinHistogram import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 5, 6, 2, 3]]
    # output: 10
    # EXPLANATION:  The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.
    ,
    # example 2
    [[2, 4]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
