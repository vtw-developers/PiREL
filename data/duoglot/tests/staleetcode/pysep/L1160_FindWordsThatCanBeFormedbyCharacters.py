### countCharacters 
from collections import Counter
from typing import *
def f_gold(words: List[str], chars: str) -> int:
    counter = Counter(chars)
    ans = 0
    for word in words:
        cnt = Counter(word)
        if all([counter[c] >= v for c, v in cnt.items()]):
            ans += len(word)
    return ans