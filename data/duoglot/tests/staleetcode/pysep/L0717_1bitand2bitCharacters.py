### isOneBitCharacter 
from typing import *
def f_gold(bits: List[int]) -> bool:
    i, n = 0, len(bits)
    while i < n - 1:
        i += bits[i] + 1
    return i == n - 1