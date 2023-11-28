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