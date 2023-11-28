
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 5, 6, 7, 0, 1, 2], 0]
    # output: 4
    ,
    # example 2
    [[4, 5, 6, 7, 0, 1, 2], 3]
    # output: -1
    ,
    # example 3
    [[1], 0]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### search 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[0] <= nums[mid]:
            if nums[0] <= target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[n - 1]:
                left = mid + 1
            else:
                right = mid
    return left if nums[left] == target else -1
"-----------------"
test()

