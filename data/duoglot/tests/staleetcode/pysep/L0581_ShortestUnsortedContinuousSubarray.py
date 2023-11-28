### findUnsortedSubarray 
from typing import *
def f_gold(nums: List[int]) -> int:
    arr = sorted(nums)
    left, right = 0, len(nums) - 1
    while left <= right and nums[left] == arr[left]:
        left += 1
    while left <= right and nums[right] == arr[right]:
        right -= 1
    return right - left + 1