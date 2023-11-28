### constrainedSubsetSum 
import math
from math import inf
from collections import deque
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    ans = float('-inf')
    q = deque()
    for i, v in enumerate(nums):
        if q and i - q[0] > k:
            q.popleft()
        dp[i] = max(0, 0 if not q else dp[q[0]]) + v
        while q and dp[q[-1]] <= dp[i]:
            q.pop()
        q.append(i)
        ans = max(ans, dp[i])
    return ans