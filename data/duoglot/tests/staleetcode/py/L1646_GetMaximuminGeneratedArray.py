
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7]
    # output: 3
    # EXPLANATION:  According to the given rules:   nums[0] = 0   nums[1] = 1   nums[(1 * 2) = 2] = nums[1] = 1   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2   nums[(2 * 2) = 4] = nums[2] = 1   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3   nums[(3 * 2) = 6] = nums[3] = 2   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3 Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.
    ,
    # example 2
    [2]
    # output: 1
    # EXPLANATION:  According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.
    ,
    # example 3
    [3]
    # output: 2
    # EXPLANATION:  According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### getMaximumGenerated 
from typing import *
def f_gold(n: int) -> int:
    if n == 0:
        return 0
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i >> 1] if i % 2 == 0 else nums[i >> 1] + nums[(i >> 1) + 1]
    return max(nums)
"-----------------"
test()

