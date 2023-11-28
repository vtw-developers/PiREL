### trailingZeroes 
from typing import *
def f_gold(n: int) -> int:
    ans = 0
    while n:
        n //= 5
        ans += n
    return ans