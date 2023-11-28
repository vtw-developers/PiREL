### minimumRounds 
from collections import Counter
from typing import *
def f_gold(tasks: List[int]) -> int:
    cnt = Counter(tasks)
    mi = min(cnt.values())
    if mi == 1:
        return -1
    return sum(v // 3 + (0 if v % 3 == 0 else 1) for v in cnt.values())