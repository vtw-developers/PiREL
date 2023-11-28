### rob 
from typing import *
def f_gold(nums: List[int]) -> int:
    def f_goldRange(nums, l, r):
        a, b = 0, nums[l]
        for num in nums[l + 1 : r + 1]:
            a, b = b, max(num + a, b)
        return b
    n = len(nums)
    if n == 1:
        return nums[0]
    s1, s2 = f_goldRange(nums, 0, n - 2), f_goldRange(nums, 1, n - 1)
    return max(s1, s2)