
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]]
    # output: 2
    # EXPLANATION:  There is one obstacle in the middle of the 3x3 grid above. There are two ways to reach the bottom-right corner: 1. Right -> Right -> Down -> Down 2. Down -> Down -> Right -> Right
    ,
    # example 2
    [[[0, 1], [0, 0]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### uniquePathsWithObstacles 
from typing import *
def f_gold(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
"-----------------"
test()

