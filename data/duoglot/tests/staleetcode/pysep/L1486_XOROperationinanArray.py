### xorOperation 
from typing import *
def f_gold(n: int, start: int) -> int:
    res = 0
    for i in range(n):
        res ^= start + (i << 1)
    return res