### isPalindrome 
from typing import *
def f_gold(x: int) -> bool:
    if x < 0:
        return False
    y, t = 0, x
    while t:
        y = y * 10 + t % 10
        t //= 10
    return x == y