### searchInsert 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left