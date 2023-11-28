### largestWordCount 
from collections import Counter
from typing import *
def f_gold(messages: List[str], senders: List[str]) -> str:
    cnt = Counter()
    for m, s in zip(messages, senders):
        cnt[s] += m.count(' ') + 1
    return sorted(cnt.items(), key=lambda x: (x[1], x[0]))[-1][0]