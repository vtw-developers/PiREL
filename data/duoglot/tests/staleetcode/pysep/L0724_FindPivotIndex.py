### pivotIndex 
from typing import *
def f_gold(nums: List[int]) -> int:
    s, presum = sum(nums), 0
    for i, v in enumerate(nums):
        if (presum << 1) == s - v:
            return i
        presum += v
    return -1