from L0733_FloodFill import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2]
    # output: [[2,2,2],[2,2,0],[2,0,1]]
    # EXPLANATION:  From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color. Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
    ,
    # example 2
    [[[0, 0, 0], [0, 0, 0]], 0, 0, 0]
    # output: [[0,0,0],[0,0,0]]
    # EXPLANATION:  The starting pixel is already colored 0, so no changes are made to the image.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
