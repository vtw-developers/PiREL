### minOperations 
import math
from math import inf
from typing import *
def f_gold(nums: List[int], x: int) -> int:
    x = sum(nums) - x
    n = len(nums)
    s = 0
    seen = {0: -1}
    ans = float('inf')
    for i, v in enumerate(nums):
        s += v
        if s not in seen:
            seen[s] = i
        if s - x in seen:
            j = seen[s - x]
            ans = min(ans, n - (i - j))
    return -1 if ans == float('inf') else ans