
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 4, 2, 2]]
    # output: 2
    ,
    # example 2
    [[3, 1, 3, 4, 2]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDuplicate 
from typing import *
def f_gold(nums: List[int]) -> int:
    left, right = 1, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        cnt = sum(v <= mid for v in nums)
        if cnt > mid:
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

