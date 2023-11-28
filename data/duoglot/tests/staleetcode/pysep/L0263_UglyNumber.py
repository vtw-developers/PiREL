### isUgly 
from typing import *
def f_gold(n: int) -> bool:
    if n < 1:
        return False
    for x in [2, 3, 5]:
        while n % x == 0:
            n //= x
    return n == 1