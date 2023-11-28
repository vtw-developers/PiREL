
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 2, 1, -4], 1]
    # output: 2
    # EXPLANATION:  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    ,
    # example 2
    [[0, 0, 0], 1]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### threeSumClosest 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    def twoSumClosest(nums, start, end, target):
        res = 0
        diff = 10000
        while start < end:
            val = nums[start] + nums[end]
            if val == target:
                return val
            if abs(val - target) < diff:
                res = val
                diff = abs(val - target)
            if val < target:
                start += 1
            else:
                end -= 1
        return res
    nums.sort()
    res, n = 0, len(nums)
    diff = 10000
    for i in range(n - 2):
        t = twoSumClosest(nums, i + 1, n - 1, target - nums[i])
        if abs(nums[i] + t - target) < diff:
            res = nums[i] + t
            diff = abs(nums[i] + t - target)
    return res
"-----------------"
test()

