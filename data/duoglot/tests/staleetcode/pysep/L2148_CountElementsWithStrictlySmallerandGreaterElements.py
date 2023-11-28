### countElements 
from typing import *
def f_gold(nums: List[int]) -> int:
    mi, mx = min(nums), max(nums)
    return sum(mi < num < mx for num in nums)