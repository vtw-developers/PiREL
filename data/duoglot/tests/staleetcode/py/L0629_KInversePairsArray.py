
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 0]
    # output: 1
    # EXPLANATION:  Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
    ,
    # example 2
    [3, 1]
    # output: 2
    # EXPLANATION:  The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kInversePairs 
from typing import *
def f_gold(n: int, k: int) -> int:
    mod = 1000000007
    dp, pre = [0] * (k + 1), [0] * (k + 2)
    for i in range(1, n + 1):
        dp[0] = 1
        # dp[i][j] = dp[i - 1][j - (i - 1)] + ... + dp[i - 1][j]
        for j in range(1, k + 1):
            dp[j] = (pre[j + 1] - pre[max(0, j - i + 1)] + mod) % mod
        for j in range(1, k + 2):
            pre[j] = (pre[j - 1] + dp[j - 1]) % mod
    return dp[k]
"-----------------"
test()

