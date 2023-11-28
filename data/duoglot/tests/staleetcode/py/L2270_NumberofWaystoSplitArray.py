
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 4, -8, 7]]
    # output: 2
    # EXPLANATION:   There are three ways of splitting nums into two non-empty parts: - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split. - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split. - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split. Thus, the number of valid splits in nums is 2.
    ,
    # example 2
    [[2, 3, 1, 0]]
    # output: 2
    # EXPLANATION:   There are two valid splits in nums: - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split.  - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### waysToSplitArray 
from typing import *
def f_gold(nums: List[int]) -> int:
    left, right = 0, sum(nums)
    cnt = 0
    for v in nums[:-1]:
        left += v
        right -= v
        if left >= right:
            cnt += 1
    return cnt
"-----------------"
test()

