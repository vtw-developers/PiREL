### maxProduct 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> int:
    maxf = minf = res = nums[0]
    for num in nums[1:]:
        m, n = maxf, minf
        maxf = max(num, m * num, n * num)
        minf = min(num, m * num, n * num)
        res = max(res, maxf)
    return res