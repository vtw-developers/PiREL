### findMaxAverage 
from typing import *
def f_gold(nums: List[int], k: int) -> float:
    s = sum(nums[:k])
    ans = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        ans = max(ans, s)
    return ans / k