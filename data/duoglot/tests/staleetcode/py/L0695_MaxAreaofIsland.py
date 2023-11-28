
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]]
    # output: 6
    # EXPLANATION:  The answer is not 11, because the island must be connected 4-directionally.
    ,
    # example 2
    [[[0, 0, 0, 0, 0, 0, 0, 0]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxAreaOfIsland 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    def dfs(i, j):
        grid[i][j] = 0
        ans = 1
        for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                ans += dfs(x, y)
        return ans
    m, n = len(grid), len(grid[0])
    return max(
        [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1],
        default=0,
    )
"-----------------"
test()

