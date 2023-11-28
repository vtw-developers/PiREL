### makeEqual 
from collections import Counter
from typing import *
def f_gold(words: List[str]) -> bool:
    counter = Counter()
    for word in words:
        for c in word:
            counter[c] += 1
    n = len(words)
    return all(count % n == 0 for count in counter.values())