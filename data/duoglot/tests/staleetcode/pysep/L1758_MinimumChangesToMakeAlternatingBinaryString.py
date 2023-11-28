### minOperations 
from typing import *
def f_gold(s: str) -> int:
    cnt = 0
    for i, c in enumerate(s):
        cnt += c == '01'[i & 1]
    return min(cnt, len(s) - cnt)