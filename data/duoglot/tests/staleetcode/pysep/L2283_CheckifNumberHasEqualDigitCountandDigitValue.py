### digitCount 
from collections import Counter
from typing import *
def f_gold(num: str) -> bool:
    cnt = Counter(num)
    return all(int(v) == cnt[str(i)] for i, v in enumerate(num))