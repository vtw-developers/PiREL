
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]]
    # output: 35
    # EXPLANATION:  The building heights are shown in the center of the above image. The skylines when viewed from each cardinal direction are drawn in red. The grid after increasing the height of buildings without affecting skylines is: gridNew = [ [8, 4, 8, 7],             [7, 4, 7, 7],             [9, 4, 8, 7],             [3, 3, 3, 3] ]
    ,
    # example 2
    [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    # output: 0
    # EXPLANATION:  Increasing the height of any building will result in the skyline changing.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxIncreaseKeepingSkyline 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    rmx = [max(row) for row in grid]
    cmx = [max(col) for col in zip(*grid)]
    return sum(
        (min(rmx[i], cmx[j]) - grid[i][j])
        for i in range(len(grid))
        for j in range(len(grid[0]))
    )
"-----------------"
test()

