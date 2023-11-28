### minimumDifference 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    nums.sort()
    return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))