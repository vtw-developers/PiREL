### minSteps 
from collections import Counter
from typing import *
def f_gold(s: str, t: str) -> int:
    cnt = Counter(s)
    for c in t:
        cnt[c] -= 1
    return sum(abs(v) for v in cnt.values())