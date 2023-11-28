
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1], 1]
    # output: 1
    ,
    # example 2
    [[1, 2], 4]
    # output: -1
    ,
    # example 3
    [[2, -1, 2], 3]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
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
"-----------------"
test()

