from L2132_StampingtheGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 4, 3]
    # output: true
    # EXPLANATION:  We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
    ,
    # example 2
    [[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 2, 2]
    # output: false
    # EXPLANATION:  There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
