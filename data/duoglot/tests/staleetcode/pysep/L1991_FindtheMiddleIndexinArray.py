### findMiddleIndex 
from typing import *
def f_gold(nums: List[int]) -> int:
    s = sum(nums)
    total = 0
    for i, num in enumerate(nums):
        total += num
        if total - num == s - total:
            return i
    return -1