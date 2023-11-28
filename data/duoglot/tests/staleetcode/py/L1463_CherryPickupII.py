
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]]
    # output: 24
    # EXPLANATION:  Path of robot #1 and #2 are described in color green and blue respectively. Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12. Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12. Total of cherries: 12 + 12 = 24.
    ,
    # example 2
    [[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0], [1, 0, 2, 3, 0, 0, 6]]]
    # output: 28
    # EXPLANATION:  Path of robot #1 and #2 are described in color green and blue respectively. Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17. Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11. Total of cherries: 17 + 11 = 28.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### cherryPickup 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[[0] * n for _ in range(n)] for _ in range(m)]
    valid = [[[False] * n for _ in range(n)] for _ in range(m)]
    dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]
    valid[0][0][n - 1] = True
    for i in range(1, m):
        for j1 in range(n):
            for j2 in range(n):
                t = grid[i][j1]
                if j1 != j2:
                    t += grid[i][j2]
                ok = False
                for y1 in range(j1 - 1, j1 + 2):
                    for y2 in range(j2 - 1, j2 + 2):
                        if 0 <= y1 < n and 0 <= y2 < n and valid[i - 1][y1][y2]:
                            dp[i][j1][j2] = max(
                                dp[i][j1][j2], dp[i - 1][y1][y2] + t
                            )
                            ok = True
                valid[i][j1][j2] = ok
    return max(dp[m - 1][j1][j2] for j1 in range(n) for j2 in range(n))
"-----------------"
test()

