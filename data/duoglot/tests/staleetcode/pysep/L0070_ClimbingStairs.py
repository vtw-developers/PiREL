### climbStairs 
from typing import *
def f_gold(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b