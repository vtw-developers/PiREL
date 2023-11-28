### increasingTriplet 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> bool:
    mi, mid = float('inf'), float('inf')
    for num in nums:
        if num > mid:
            return True
        if num <= mi:
            mi = num
        else:
            mid = num
    return False