### minPairSum 
from typing import *
def f_gold(nums: List[int]) -> int:
    nums.sort()
    res, n = 0, len(nums)
    for i in range(n >> 1):
        res = max(res, nums[i] + nums[n - i - 1])
    return res