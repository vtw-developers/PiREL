
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, -1], [1, 0, -1], [1, 1, 1]]]
    # output: 5
    # EXPLANATION:  The player started at (0, 0) and went down, down, right right to reach (2, 2). 4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]]. Then, the player went left, up, up, left to return home, picking up one more cherry. The total number of cherries picked up is 5, and this is the maximum possible.
    ,
    # example 2
    [[[1, 1, -1], [1, -1, 1], [-1, 1, 1]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### cherryPickup 
import math
from math import inf
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    n = len(grid)
    dp = [[[float('-inf')] * n for _ in range(n)] for _ in range((n << 1) - 1)]
    dp[0][0][0] = grid[0][0]
    for k in range(1, (n << 1) - 1):
        for i1 in range(n):
            for i2 in range(n):
                j1, j2 = k - i1, k - i2
                if (
                    not 0 <= j1 < n
                    or not 0 <= j2 < n
                    or grid[i1][j1] == -1
                    or grid[i2][j2] == -1
                ):
                    continue
                t = grid[i1][j1]
                if i1 != i2:
                    t += grid[i2][j2]
                for x1 in range(i1 - 1, i1 + 1):
                    for x2 in range(i2 - 1, i2 + 1):
                        if x1 >= 0 and x2 >= 0:
                            dp[k][i1][i2] = max(
                                dp[k][i1][i2], dp[k - 1][x1][x2] + t
                            )
    return max(0, dp[-1][-1][-1])
"-----------------"
test()

