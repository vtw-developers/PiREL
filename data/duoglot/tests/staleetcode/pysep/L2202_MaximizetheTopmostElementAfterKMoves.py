### maximumTop 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    if k == 0:
        return nums[0]
    n = len(nums)
    if n == 1:
        if k % 2:
            return -1
        return nums[0]
    ans = max(nums[: k - 1], default=-1)
    if k < n:
        ans = max(ans, nums[k])
    return ans