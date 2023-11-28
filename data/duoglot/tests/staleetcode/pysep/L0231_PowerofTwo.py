### isPowerOfTwo 
from typing import *
def f_gold(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0