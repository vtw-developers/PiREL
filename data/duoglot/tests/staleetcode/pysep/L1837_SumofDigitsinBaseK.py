### sumBase 
from typing import *
def f_gold(n: int, k: int) -> int:
    res = 0
    while n != 0:
        n, t = divmod(n, k)
        res += t
    return res