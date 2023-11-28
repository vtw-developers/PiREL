from L1725_NumberOfRectanglesThatCanFormTheLargestSquare import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[5, 8], [3, 9], [5, 12], [16, 5]]]
    # output: 3
    # EXPLANATION:  The largest squares you can get from each rectangle are of lengths [5,3,5,5].  The largest possible square is of length 5, and you can get it out of 3 rectangles.
    ,
    # example 2
    [[[2, 3], [3, 7], [4, 3], [3, 7]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
