### hasAlternatingBits 
from typing import *
def f_gold(n: int) -> bool:
    n ^= n >> 1
    return (n & (n + 1)) == 0