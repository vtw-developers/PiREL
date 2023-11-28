
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 1, 0]]
    # output: 4
    # EXPLANATION:  Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
    ,
    # example 2
    [[1, 0, 1, 1, 0, 1]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMaxConsecutiveOnes 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    prefix = [0] * n
    suffix = [0] * n
    res = 0
    for i in range(n):
        if i == 0:
            prefix[i] = nums[i]
        else:
            prefix[i] = 0 if nums[i] == 0 else prefix[i - 1] + 1
        res = max(res, prefix[i])
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            suffix[i] = nums[i]
        else:
            suffix[i] = 0 if nums[i] == 0 else suffix[i + 1] + 1
    for i in range(n):
        if nums[i] == 0:
            t = 1
            if i > 0:
                t += prefix[i - 1]
            if i < n - 1:
                t += suffix[i + 1]
            res = max(res, t)
    return res
"-----------------"
test()

