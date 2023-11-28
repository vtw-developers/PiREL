
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]]
    # output: 1
    ,
    # example 2
    [[[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numDistinctIslands 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def dfs(i, j, direction, path):
        grid[i][j] = 0
        path.append(str(direction))
        dirs = [-1, 0, 1, 0, -1]
        for k in range(1, 5):
            x, y = i + dirs[k - 1], j + dirs[k]
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                dfs(x, y, k, path)
        path.append(str(-direction))
    paths = set()
    path = []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, 0, path)
                paths.add(''.join(path))
                path.clear()
    return len(paths)
"-----------------"
test()

