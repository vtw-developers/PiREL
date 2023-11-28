### maxSubsequence 
from typing import *
def f_gold(nums: List[int], k: int) -> List[int]:
    idx = list(range(len(nums)))
    idx.sort(key=lambda i: nums[i])
    return [nums[i] for i in sorted(idx[-k:])]