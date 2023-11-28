
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 1]]
    # output: 2
    # EXPLANATION:  3 is a peak element and your function should return the index number 2.
    ,
    # example 2
    [[1, 2, 1, 3, 5, 6, 4]]
    # output: 5
    # EXPLANATION:  Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findPeakElement 
from typing import *
def f_gold(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

