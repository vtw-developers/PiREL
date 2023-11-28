### judgeSquareSum 
import math
from math import sqrt
from typing import *
def f_gold(c: int) -> bool:
    a, b = 0, int(sqrt(c))
    while a <= b:
        s = a**2 + b**2
        if s == c:
            return True
        if s < c:
            a += 1
        else:
            b -= 1
    return False