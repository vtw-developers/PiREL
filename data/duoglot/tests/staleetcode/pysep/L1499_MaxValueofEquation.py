### findMaxValueOfEquation 
import math
from math import inf
from collections import deque
from typing import *
def f_gold(points: List[List[int]], k: int) -> int:
    q = deque([points[0]])
    ans = float('-inf')
    for x, y in points[1:]:
        while q and x - q[0][0] > k:
            q.popleft()
        if q:
            ans = max(ans, x + y + q[0][1] - q[0][0])
        while q and y - x > q[-1][1] - q[-1][0]:
            q.pop()
        q.append([x, y])
    return ans