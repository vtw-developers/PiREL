
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 2, -10, 5, 20], 2]
    # output: 37
    # EXPLANATION:  The subsequence is [10, 2, 5, 20].
    ,
    # example 2
    [[-1, -2, -3], 1]
    # output: -1
    # EXPLANATION:  The subsequence must be non-empty, so we choose the largest number.
    ,
    # example 3
    [[10, -2, -10, -5, 20], 2]
    # output: 23
    # EXPLANATION:  The subsequence is [10, -2, -5, 20].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
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
"-----------------"
test()

