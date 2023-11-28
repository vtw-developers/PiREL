### findingUsersActiveMinutes 
from collections import defaultdict
from typing import *
def f_gold(logs: List[List[int]], k: int) -> List[int]:
    d = defaultdict(set)
    for u, t in logs:
        d[u].add(t)
    ans = [0] * k
    for ts in d.values():
        ans[len(ts) - 1] += 1
    return ans