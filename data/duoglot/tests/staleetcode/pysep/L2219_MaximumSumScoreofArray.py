### maximumSumScore 
from itertools import accumulate
from typing import *
def f_gold(nums: List[int]) -> int:
    s = [0] + list(accumulate(nums))
    return max(max(s[i + 1], s[-1] - s[i]) for i in range(len(nums)))