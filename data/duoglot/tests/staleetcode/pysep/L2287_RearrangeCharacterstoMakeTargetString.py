### rearrangeCharacters 
import math
from math import inf
from collections import Counter
from typing import *
def f_gold(s: str, target: str) -> int:
    cnt = Counter(s)
    cnt2 = Counter(target)
    ans = float('inf')
    for c, v in cnt2.items():
        if cnt[c] < v:
            return 0
        ans = min(ans, cnt[c] // v)
    return ans