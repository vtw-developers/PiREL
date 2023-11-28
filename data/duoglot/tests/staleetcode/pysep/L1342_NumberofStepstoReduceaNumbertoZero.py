### numberOfSteps 
from typing import *
def f_gold(num: int) -> int:
    ans = 0
    while num:
        if num & 1:
            num -= 1
        else:
            num >>= 1
        ans += 1
    return ans