### minStartValue 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> int:
    s, t = 0, float('inf')
    for num in nums:
        s += num
        t = min(t, s)
    return max(1, 1 - t)