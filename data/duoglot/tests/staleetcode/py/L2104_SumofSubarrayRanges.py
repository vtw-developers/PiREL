
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 4
    # EXPLANATION:  The 6 subarrays of nums are the following: [1], range = largest - smallest = 1 - 1 = 0  [2], range = 2 - 2 = 0 [3], range = 3 - 3 = 0 [1,2], range = 2 - 1 = 1 [2,3], range = 3 - 2 = 1 [1,2,3], range = 3 - 1 = 2 So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
    ,
    # example 2
    [[1, 3, 3]]
    # output: 4
    # EXPLANATION:  The 6 subarrays of nums are the following: [1], range = largest - smallest = 1 - 1 = 0 [3], range = 3 - 3 = 0 [3], range = 3 - 3 = 0 [1,3], range = 3 - 1 = 2 [3,3], range = 3 - 3 = 0 [1,3,3], range = 3 - 1 = 2 So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
    ,
    # example 3
    [[4, -2, -3, 4, 1]]
    # output: 59
    # EXPLANATION:  The sum of all subarray ranges of nums is 59.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### subArrayRanges 
from typing import *
def f_gold(nums: List[int]) -> int:
    def f(nums):
        stk = []
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] <= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        return sum((i - left[i]) * (right[i] - i) * v for i, v in enumerate(nums))
    mx = f(nums)
    mi = f([-v for v in nums])
    return mx + mi
"-----------------"
test()

