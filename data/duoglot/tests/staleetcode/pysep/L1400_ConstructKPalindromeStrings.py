### canConstruct 
from collections import Counter
from typing import *
def f_gold(s: str, k: int) -> bool:
    if len(s) < k:
        return False
    counter = Counter(s)
    cnt = sum(1 for n in counter.values() if n % 2 == 1)
    return cnt <= k