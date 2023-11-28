
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [1, 2]], 0, 0, 3]
    # output: [[3,3],[3,2]]
    ,
    # example 2
    [[[1, 2, 2], [2, 3, 2]], 0, 1, 3]
    # output: [[1,3,3],[2,3,3]]
    ,
    # example 3
    [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2]
    # output: [[2,2,2],[2,1,2],[2,2,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### colorBorder 
from typing import *
def f_gold(grid: List[List[int]], row: int, col: int, color: int
) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    vis = [[False] * n for _ in range(m)]
    def dfs(i, j, color):
        vis[i][j] = True
        old_color = grid[i][j]
        for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = a + i, b + j
            if 0 <= x < m and 0 <= y < n:
                if not vis[x][y]:
                    if grid[x][y] == old_color:
                        dfs(x, y, color)
                    else:
                        grid[i][j] = color
            else:
                grid[i][j] = color
    dfs(row, col, color)
    return grid
"-----------------"
test()

