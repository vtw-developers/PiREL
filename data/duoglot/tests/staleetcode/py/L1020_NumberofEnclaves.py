
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]]
    # output: 3
    # EXPLANATION:  There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
    ,
    # example 2
    [[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]]
    # output: 0
    # EXPLANATION:  All 1s are either on the boundary or can reach the boundary.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numEnclaves 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def dfs(i, j):
        grid[i][j] = 0
        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                dfs(x, y)
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                dfs(i, j)
    return sum(grid[i][j] for i in range(m) for j in range(n))
"-----------------"
test()

