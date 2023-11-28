### shortestToChar 
import math
from math import inf
from typing import *
def f_gold(s: str, c: str) -> List[int]:
    n = len(s)
    ans = [0] * n
    j = float('inf')
    for i, ch in enumerate(s):
        if ch == c:
            j = i
        ans[i] = abs(i - j)
    j = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            j = i
        ans[i] = min(ans[i], abs(i - j))
    return ans