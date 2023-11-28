### countOperations 
from typing import *
def f_gold(num1: int, num2: int) -> int:
    ans = 0
    while num1 and num2:
        if num1 >= num2:
            num1, num2 = num2, num1
        num2 -= num1
        ans += 1
    return ans