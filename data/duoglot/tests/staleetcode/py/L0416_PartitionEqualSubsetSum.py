
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 5, 11, 5]]
    # output: true
    # EXPLANATION:  The array can be partitioned as [1, 5, 5] and [11].
    ,
    # example 2
    [[1, 2, 3, 5]]
    # output: false
    # EXPLANATION:  The array cannot be partitioned into equal sum subsets.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canPartition 
from typing import *
def f_gold(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False
    n = s >> 1
    dp = [False] * (n + 1)
    dp[0] = True
    for v in nums:
        for j in range(n, v - 1, -1):
            dp[j] = dp[j] or dp[j - v]
    return dp[-1]
"-----------------"
test()

