### moveZeroes 
from typing import *
def f_gold(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, n = 0, len(nums)
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1