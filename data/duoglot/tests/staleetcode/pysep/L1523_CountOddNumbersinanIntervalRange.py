### countOdds 
from typing import *
def f_gold(low: int, high: int) -> int:
    return ((high + 1) >> 1) - (low >> 1)