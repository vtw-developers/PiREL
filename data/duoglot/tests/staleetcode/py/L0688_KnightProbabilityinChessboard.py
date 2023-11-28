
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 2, 0, 0]
    # output: 0.06250
    # EXPLANATION:  There are two moves (to (1,2), (2,1)) that will keep the knight on the board. From each of those positions, there are also two moves that will keep the knight on the board. The total probability the knight stays on the board is 0.0625.
    ,
    # example 2
    [1, 0, 0, 0]
    # output: 1.00000
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### knightProbability 
from typing import *
def f_gold(n: int, k: int, row: int, column: int) -> float:
    dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
    for l in range(k + 1):
        for i in range(n):
            for j in range(n):
                if l == 0:
                    dp[l][i][j] = 1
                else:
                    for a, b in (
                        (-2, -1),
                        (-2, 1),
                        (2, -1),
                        (2, 1),
                        (-1, -2),
                        (-1, 2),
                        (1, -2),
                        (1, 2),
                    ):
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n:
                            dp[l][i][j] += dp[l - 1][x][y] / 8
    return dp[k][row][column]
"-----------------"
test()

