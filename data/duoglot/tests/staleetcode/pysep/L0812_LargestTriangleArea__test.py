from L0812_LargestTriangleArea import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]]
    # output: 2.00000
    # EXPLANATION:  The five points are shown in the above figure. The red triangle is the largest.
    ,
    # example 2
    [[[1, 0], [0, 0], [0, 1]]]
    # output: 0.50000
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
