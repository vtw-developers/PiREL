### smallestRangeI 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    mx, mi = max(nums), min(nums)
    return max(0, mx - mi - k * 2)