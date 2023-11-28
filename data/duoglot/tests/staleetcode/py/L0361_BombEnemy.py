
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]]
    # output: 3
    ,
    # example 2
    [[["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxKilledEnemies 
from typing import *
def f_gold(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    g = [[0] * n for _ in range(m)]
    for i in range(m):
        t = 0
        for j in range(n):
            if grid[i][j] == 'W':
                t = 0
            elif grid[i][j] == 'E':
                t += 1
            g[i][j] += t
        t = 0
        for j in range(n - 1, -1, -1):
            if grid[i][j] == 'W':
                t = 0
            elif grid[i][j] == 'E':
                t += 1
            g[i][j] += t
    for j in range(n):
        t = 0
        for i in range(m):
            if grid[i][j] == 'W':
                t = 0
            elif grid[i][j] == 'E':
                t += 1
            g[i][j] += t
        t = 0
        for i in range(m - 1, -1, -1):
            if grid[i][j] == 'W':
                t = 0
            elif grid[i][j] == 'E':
                t += 1
            g[i][j] += t
    return max(
        [g[i][j] for i in range(m) for j in range(n) if grid[i][j] == '0'],
        default=0,
    )
"-----------------"
test()

