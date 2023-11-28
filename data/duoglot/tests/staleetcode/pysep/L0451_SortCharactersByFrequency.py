### frequencySort 
from collections import defaultdict
from collections import Counter
from typing import *
def f_gold(s: str) -> str:
    counter = Counter(s)
    buckets = defaultdict(list)
    for c, freq in counter.items():
        buckets[freq].append(c)
    res = []
    for i in range(len(s), -1, -1):
        if buckets[i]:
            for c in buckets[i]:
                res.append(c * i)
    return ''.join(res)