### countPoints 
from collections import defaultdict
from typing import *
def f_gold(rings: str) -> int:
    mp = defaultdict(set)
    for i in range(1, len(rings), 2):
        c = int(rings[i])
        mp[c].add(rings[i - 1])
    return sum(len(v) == 3 for v in mp.values())