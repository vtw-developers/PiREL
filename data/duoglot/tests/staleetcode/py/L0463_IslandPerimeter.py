
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]]
    # output: 16
    # EXPLANATION:  The perimeter is the 16 yellow stripes in the image above.
    ,
    # example 2
    [[[1]]]
    # output: 4
    ,
    # example 3
    [[[1, 0]]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### islandPerimeter 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ans += 4
                if i < m - 1 and grid[i + 1][j] == 1:
                    ans -= 2
                if j < n - 1 and grid[i][j + 1] == 1:
                    ans -= 2
    return ans
"-----------------"
test()

