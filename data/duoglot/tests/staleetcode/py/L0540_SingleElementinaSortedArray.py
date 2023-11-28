
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 3, 3, 4, 4, 8, 8]]
    # output: 2
    ,
    # example 2
    [[3, 3, 7, 7, 10, 11, 11]]
    # output: 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### singleNonDuplicate 
from typing import *
def f_gold(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        # Equals to: if (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 == 1 and nums[mid] != nums[mid - 1]):
        if nums[mid] != nums[mid ^ 1]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
"-----------------"
test()

