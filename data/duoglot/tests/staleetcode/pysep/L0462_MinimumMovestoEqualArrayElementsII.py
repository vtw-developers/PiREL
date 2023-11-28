### minMoves2 
from typing import *
def f_gold(nums: List[int]) -> int:
    nums.sort()
    k = nums[len(nums) >> 1]
    return sum(abs(v - k) for v in nums)