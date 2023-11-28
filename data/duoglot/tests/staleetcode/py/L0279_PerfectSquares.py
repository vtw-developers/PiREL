
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [12]
    # output: 3
    # EXPLANATION:  12 = 4 + 4 + 4.
    ,
    # example 2
    [13]
    # output: 2
    # EXPLANATION:  13 = 4 + 9.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSquares 
import math
from math import inf
from typing import *
def f_gold(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        j, mi = 1, float('inf')
        while j * j <= i:
            mi = min(mi, dp[i - j * j])
            j += 1
        dp[i] = mi + 1
    return dp[-1]
"-----------------"
test()

