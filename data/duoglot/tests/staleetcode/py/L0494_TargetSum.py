
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 1, 1], 3]
    # output: 5
    # EXPLANATION:  There are 5 ways to assign symbols to make the sum of nums be target 3. -1 + 1 + 1 + 1 + 1 = 3 +1 - 1 + 1 + 1 + 1 = 3 +1 + 1 - 1 + 1 + 1 = 3 +1 + 1 + 1 - 1 + 1 = 3 +1 + 1 + 1 + 1 - 1 = 3
    ,
    # example 2
    [[1], 1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findTargetSumWays 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    s = sum(nums)
    if s < target or (s - target) % 2 != 0:
        return 0
    n = (s - target) // 2
    dp = [0] * (n + 1)
    dp[0] = 1
    for v in nums:
        for j in range(n, v - 1, -1):
            dp[j] += dp[j - v]
    return dp[-1]
"-----------------"
test()

