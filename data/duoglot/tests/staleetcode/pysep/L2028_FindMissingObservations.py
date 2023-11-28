### missingRolls 
from typing import *
def f_gold(rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    s = (n + m) * mean - sum(rolls)
    if s > n * 6 or s < n:
        return []
    ans = [s // n] * n
    for i in range(s % n):
        ans[i] += 1
    return ans