### twoSumLessThanK 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    nums.sort()
    low, high = 0, len(nums) - 1
    res = -1
    while low < high:
        val = nums[low] + nums[high]
        if val < k:
            res = max(res, val)
            low += 1
        else:
            high -= 1
    return res