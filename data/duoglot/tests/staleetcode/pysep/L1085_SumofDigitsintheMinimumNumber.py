### sumOfDigits 
from typing import *
def f_gold(nums: List[int]) -> int:
    x = min(nums)
    s = 0
    while x:
        s += x % 10
        x //= 10
    return 0 if s % 2 else 1