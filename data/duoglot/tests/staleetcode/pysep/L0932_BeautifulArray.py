### beautifulArray 
from typing import *
def f_gold(n: int) -> List[int]:
    if n == 1:
        return [1]
    left = f_gold((n + 1) >> 1)
    right = f_gold(n >> 1)
    left = [x * 2 - 1 for x in left]
    right = [x * 2 for x in right]
    return left + right