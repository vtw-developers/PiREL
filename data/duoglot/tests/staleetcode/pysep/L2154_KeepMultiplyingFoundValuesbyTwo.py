### findFinalValue 
from typing import *
def f_gold(nums: List[int], original: int) -> int:
    s = set(nums)
    while original in s:
        original <<= 1
    return original