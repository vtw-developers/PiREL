
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 7, 4, 1, 8, 1]]
    # output: 1
    # EXPLANATION:  We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then, we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then, we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then, we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
    ,
    # example 2
    [[31, 26, 33, 21, 40]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lastStoneWeightII 
from typing import *
def f_gold(stones: List[int]) -> int:
    s = sum(stones)
    m, n = len(stones), s >> 1
    dp = [0] * (n + 1)
    for v in stones:
        for j in range(n, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + v)
    return s - dp[-1] * 2
"-----------------"
test()

