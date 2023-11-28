
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: 3
    # EXPLANATION:  We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
    ,
    # example 2
    [[1]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfArithmeticSlices 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * n
    for i in range(2, n):
        if nums[i] + nums[i - 2] == (nums[i - 1] << 1):
            dp[i] = 1 + dp[i - 1]
    return sum(dp)
"-----------------"
test()

