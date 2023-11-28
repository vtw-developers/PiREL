### firstUniqChar 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    counter = Counter(s)
    for i, c in enumerate(s):
        if counter[c] == 1:
            return i
    return -1