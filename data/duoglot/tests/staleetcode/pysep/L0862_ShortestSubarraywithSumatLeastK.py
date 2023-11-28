### shortestSubarray 
from itertools import accumulate
import math
from math import inf
from collections import deque
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    s = [0] + list(accumulate(nums))
    ans = float('inf')
    q = deque([0])
    for i in range(1, len(s)):
        while q and s[i] - s[q[0]] >= k:
            ans = min(ans, i - q.popleft())
        while q and s[i] <= s[q[-1]]:
            q.pop()
        q.append(i)
    return -1 if ans == float('inf') else ans