### maxScore 
import math
from math import inf
from typing import *
def f_gold(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + cardPoints[i]
    mi = float('inf')
    for i in range(n):
        j = i + (n - k) - 1
        if j < n:
            mi = min(mi, s[j + 1] - s[i])
    return s[-1] - mi