### numJewelsInStones 
from typing import *
def f_gold(jewels: str, stones: str) -> int:
    s = set(jewels)
    return sum([1 for c in stones if c in s])