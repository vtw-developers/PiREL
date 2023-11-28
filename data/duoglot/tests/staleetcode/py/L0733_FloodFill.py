
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


"-----------------"
### floodFill 
from typing import *
def f_gold(image: List[List[int]], sr: int, sc: int, newColor: int
) -> List[List[int]]:
    def dfs(i, j, oc, nc):
        if (
            i < 0
            or i >= len(image)
            or j < 0
            or j >= len(image[0])
            or image[i][j] != oc
            or image[i][j] == nc
        ):
            return
        image[i][j] = nc
        for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            dfs(i + x, j + y, oc, nc)
    dfs(sr, sc, image[sr][sc], newColor)
    return image
"-----------------"
test()

