### deleteAndEarn 
import math
from math import inf
from typing import *
def f_gold(nums: List[int]) -> int:
    mx = float('-inf')
    for num in nums:
        mx = max(mx, num)
    total = [0] * (mx + 1)
    for num in nums:
        total[num] += num
    first = total[0]
    second = max(total[0], total[1])
    for i in range(2, mx + 1):
        cur = max(first + total[i], second)
        first = second
        second = cur
    return second