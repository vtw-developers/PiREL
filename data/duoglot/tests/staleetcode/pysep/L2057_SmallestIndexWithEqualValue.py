### smallestEqual 
from typing import *
def f_gold(nums: List[int]) -> int:
    for i, v in enumerate(nums):
        if i % 10 == v:
            return i
    return -1