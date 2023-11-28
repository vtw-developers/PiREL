### reorderedPowerOf2 
from typing import *
def f_gold(n: int) -> bool:
    def convert(n):
        counter = [0] * 10
        while n > 0:
            counter[n % 10] += 1
            n //= 10
        return counter
    i, s = 1, convert(n)
    while i <= 10**9:
        if convert(i) == s:
            return True
        i <<= 1
    return False