### minSteps 
from collections import Counter
from typing import *
def f_gold(s: str, t: str) -> int:
    counter = Counter(s)
    res = 0
    for c in t:
        if counter[c] > 0:
            counter[c] -= 1
        else:
            res += 1
    return res