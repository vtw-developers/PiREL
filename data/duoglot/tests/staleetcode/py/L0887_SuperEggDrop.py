
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2]
    # output: 2
    # EXPLANATION:  Drop the egg from floor 1. If it breaks, we know that f = 0. Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1. If it does not break, then we know f = 2. Hence, we need at minimum 2 moves to determine with certainty what the value of f is.
    ,
    # example 2
    [2, 6]
    # output: 3
    ,
    # example 3
    [3, 14]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### superEggDrop 
from typing import *
def f_gold(K: int, N: int) -> int:
    dp = [1] * (K)
    while dp[K - 1] < N:
        for i in range(K - 1, 0, -1):
            dp[i] = dp[i] + dp[i - 1] + 1
        dp[0] = dp[0] + 1
    return dp[0]
"-----------------"
test()

