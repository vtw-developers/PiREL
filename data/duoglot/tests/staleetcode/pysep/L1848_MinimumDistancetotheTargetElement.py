### getMinDistance 
import math
from math import inf
from typing import *
def f_gold(nums: List[int], target: int, start: int) -> int:
    res = float('inf')
    for i, num in enumerate(nums):
        if num == target:
            res = min(res, abs(i - start))
    return res