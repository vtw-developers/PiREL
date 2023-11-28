### repeatedStringMatch 
import math
from math import ceil
from typing import *
def f_gold(a: str, b: str) -> int:
    m, n = len(a), len(b)
    ans = ceil(n / m)
    t = [a] * ans
    for _ in range(3):
        if b in ''.join(t):
            return ans
        ans += 1
        t.append(a)
    return -1