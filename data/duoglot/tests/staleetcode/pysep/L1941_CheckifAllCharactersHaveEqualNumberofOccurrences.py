### areOccurrencesEqual 
from collections import Counter
from typing import *
def f_gold(s: str) -> bool:
    cnt = Counter(s)
    return len(set(cnt.values())) == 1