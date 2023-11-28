### rangeBitwiseAnd 
from typing import *
def f_gold(left: int, right: int) -> int:
    while left < right:
        right &= right - 1
    return right