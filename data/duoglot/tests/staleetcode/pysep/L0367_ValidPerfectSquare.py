### isPerfectSquare 
from typing import *
def f_gold(num: int) -> bool:
    left, right = 1, num
    while left < right:
        mid = (left + right) >> 1
        if mid * mid >= num:
            right = mid
        else:
            left = mid + 1
    return left * left == num