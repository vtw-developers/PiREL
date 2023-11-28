### numSubarrayProductLessThanK 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    ans, s, j = 0, 1, 0
    for i, v in enumerate(nums):
        s *= v
        while j <= i and s >= k:
            s //= nums[j]
            j += 1
        ans += i - j + 1
    return ans