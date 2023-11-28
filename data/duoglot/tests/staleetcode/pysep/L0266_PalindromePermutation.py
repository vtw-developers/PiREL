### canPermutePalindrome 
from collections import Counter
from typing import *
def f_gold(s: str) -> bool:
    counter = Counter(s)
    return sum(e % 2 for e in counter.values()) < 2