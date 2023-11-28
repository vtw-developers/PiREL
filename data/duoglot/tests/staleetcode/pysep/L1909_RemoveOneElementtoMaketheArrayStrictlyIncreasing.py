### canBeIncreasing 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> bool:
    def check(nums, i):
        prev = float('-inf')
        for j, num in enumerate(nums):
            if i == j:
                continue
            if prev >= nums[j]:
                return False
            prev = nums[j]
        return True
    i, n = 1, len(nums)
    while i < n and nums[i - 1] < nums[i]:
        i += 1
    return check(nums, i - 1) or check(nums, i)