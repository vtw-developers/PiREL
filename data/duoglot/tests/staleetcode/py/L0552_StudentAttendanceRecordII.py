
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2]
    # output: 8
    # EXPLANATION:  There are 8 records with length 2 that are eligible for an award: "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL" Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
    ,
    # example 2
    [1]
    # output: 3
    ,
    # example 3
    [10101]
    # output: 183236316
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkRecord 
from typing import *
def f_gold(n: int) -> int:
    mod = int(1e9 + 7)
    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n)]
    # base case
    dp[0][0][0] = dp[0][0][1] = dp[0][1][0] = 1
    for i in range(1, n):
        # A
        dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod
        # L
        dp[i][0][1] = dp[i - 1][0][0]
        dp[i][0][2] = dp[i - 1][0][1]
        dp[i][1][1] = dp[i - 1][1][0]
        dp[i][1][2] = dp[i - 1][1][1]
        # P
        dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod
        dp[i][1][0] = (
            dp[i][1][0] + dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]
        ) % mod
    ans = 0
    for j in range(2):
        for k in range(3):
            ans = (ans + dp[n - 1][j][k]) % mod
    return ans
"-----------------"
test()

