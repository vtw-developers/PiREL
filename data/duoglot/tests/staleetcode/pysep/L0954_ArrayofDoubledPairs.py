### canReorderDoubled 
from collections import Counter
from typing import *
def f_gold(arr: List[int]) -> bool:
    freq = Counter(arr)
    if freq[0] & 1:
        return False
    for x in sorted(freq, key=abs):
        if freq[x << 1] < freq[x]:
            return False
        freq[x << 1] -= freq[x]
    return True