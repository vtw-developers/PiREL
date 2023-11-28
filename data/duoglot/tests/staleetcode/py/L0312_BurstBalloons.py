
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 5, 8]]
    # output: 167
    # EXPLANATION:  nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> [] coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
    ,
    # example 2
    [[1, 5]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxCoins 
from typing import *
def f_gold(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n):
        for i in range(n - l):
            j = i + l
            for k in range(i + 1, j):
                dp[i][j] = max(
                    dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                )
    return dp[0][-1]
"-----------------"
test()

