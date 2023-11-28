### maximumDifference 
from typing import *
def f_gold(nums: List[int]) -> int:
    mi = nums[0]
    ans, n = -1, len(nums)
    for i in range(1, n):
        if nums[i] > mi:
            ans = max(ans, nums[i] - mi)
        else:
            mi = nums[i]
    return ans