### maxSubArray 
from typing import *
def f_gold(nums: List[int]) -> int:
    res = f = nums[0]
    for num in nums[1:]:
        f = num + max(f, 0)
        res = max(res, f)
    return res