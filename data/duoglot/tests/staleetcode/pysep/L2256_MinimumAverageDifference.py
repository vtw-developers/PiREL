### minimumAverageDifference 
from itertools import accumulate
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> int:
    s = list(accumulate(nums))
    ans, n = 0, len(nums)
    mi = float('inf')
    for i in range(n):
        a = s[i] // (i + 1)
        b = 0 if i == n - 1 else (s[-1] - s[i]) // (n - i - 1)
        t = abs(a - b)
        if mi > t:
            ans = i
            mi = t
    return ans