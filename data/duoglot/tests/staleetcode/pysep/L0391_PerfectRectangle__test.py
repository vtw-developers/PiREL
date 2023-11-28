from L0391_PerfectRectangle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]]
    # output: true
    # EXPLANATION:  All 5 rectangles together form an exact cover of a rectangular region.
    ,
    # example 2
    [[[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]]
    # output: false
    # EXPLANATION:  Because there is a gap between the two rectangular regions.
    ,
    # example 3
    [[[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]]
    # output: false
    # EXPLANATION:  Because two of the rectangles overlap with each other.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
