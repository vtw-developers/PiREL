### myPow 
from typing import *
def f_gold(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / f_gold(x, -n)
    y = f_gold(x, n >> 1)
    return y * y if (n & 1) == 0 else y * y * x