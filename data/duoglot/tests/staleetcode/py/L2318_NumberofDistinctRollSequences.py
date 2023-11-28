
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 184
    # EXPLANATION:  Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc. Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6). (1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed). (1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3. There are a total of 184 distinct sequences possible, so we return 184.
    ,
    # example 2
    [2]
    # output: 22
    # EXPLANATION:  Some of the possible sequences are (1, 2), (2, 1), (3, 2). Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1. There are a total of 22 distinct sequences possible, so we return 22.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### distinctSequences 
import math
from math import gcd
from typing import *
def f_gold(n: int) -> int:
    if n == 1:
        return 6
    mod = 10**9 + 7
    dp = [[[0] * 6 for _ in range(6)] for _ in range(n + 1)]
    for i in range(6):
        for j in range(6):
            if gcd(i + 1, j + 1) == 1 and i != j:
                dp[2][i][j] = 1
    for k in range(3, n + 1):
        for i in range(6):
            for j in range(6):
                if gcd(i + 1, j + 1) == 1 and i != j:
                    for h in range(6):
                        if gcd(h + 1, i + 1) == 1 and h != i and h != j:
                            dp[k][i][j] += dp[k - 1][h][i]
    ans = 0
    for i in range(6):
        for j in range(6):
            ans += dp[-1][i][j]
    return ans % mod
"-----------------"
test()

