### isConsecutive 
from typing import *
def f_gold(nums: List[int]) -> bool:
    mi, mx = min(nums), max(nums)
    n = len(nums)
    return len(set(nums)) == n and mx == mi + n - 1