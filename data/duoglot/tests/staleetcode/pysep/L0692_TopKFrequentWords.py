### topKFrequent 
from collections import Counter
from typing import *
def f_gold(words: List[str], k: int) -> List[str]:
    counter = Counter(words)
    res = sorted(counter, key=lambda word: (-counter[word], word))
    return res[:k]