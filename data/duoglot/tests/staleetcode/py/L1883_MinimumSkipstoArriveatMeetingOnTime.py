
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2], 4, 2]
    # output: 1
    # EXPLANATION:  Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours. You can skip the first rest to arrive in ((1/4 + <u>0</u>) + (3/4 + 0)) + (2/4) = 1.5 hours. Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
    ,
    # example 2
    [[7, 3, 5, 5], 2, 10]
    # output: 2
    # EXPLANATION:  Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours. You can skip the first and third rest to arrive in ((7/2 + <u>0</u>) + (3/2 + 0)) + ((5/2 + <u>0</u>) + (5/2)) = 10 hours.
    ,
    # example 3
    [[7, 3, 5, 5], 1, 10]
    # output: -1
    # EXPLANATION:  It is impossible to arrive at the meeting on time even if you skip all the rests.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSkips 
import math
from math import inf
from typing import *
def f_gold(dist: List[int], speed: int, hoursBefore: int) -> int:
    n = len(dist)
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(i + 1):
            if i != j:
                dp[i][j] = min(
                    dp[i][j],
                    ((dp[i - 1][j] + dist[i - 1] - 1) // speed + 1) * speed,
                )
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + dist[i - 1])
    for i in range(n + 1):
        if dp[n][i] <= hoursBefore * speed:
            return i
    return -1
"-----------------"
test()

