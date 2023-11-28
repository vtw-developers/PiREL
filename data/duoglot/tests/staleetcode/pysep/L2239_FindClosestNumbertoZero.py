### findClosestNumber 
from typing import *
def f_gold(nums: List[int]) -> int:
    ans, d = 0, 1000000
    for v in nums:
        if (t := abs(v)) < d or (t == d and v > ans):
            ans, d = v, t
    return ans