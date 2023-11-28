
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  All possible strings are: "a", "e", "i" , "o" and "u".
    ,
    # example 2
    [2]
    # output: 10
    # EXPLANATION:  All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
    ,
    # example 3
    [5]
    # output: 68
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countVowelPermutation 
from typing import *
def f_gold(n: int) -> int:
    dp = (1, 1, 1, 1, 1)
    MOD = 1000000007
    for _ in range(n - 1):
        dp = (
            (dp[1] + dp[2] + dp[4]) % MOD,
            (dp[0] + dp[2]) % MOD,
            (dp[1] + dp[3]) % MOD,
            dp[2],
            (dp[2] + dp[3]) % MOD,
        )
    return sum(dp) % MOD
"-----------------"
test()

