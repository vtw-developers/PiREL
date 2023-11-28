
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 4, 5, 1, 2]]
    # output: 1
    # EXPLANATION:  The original array was [1,2,3,4,5] rotated 3 times.
    ,
    # example 2
    [[4, 5, 6, 7, 0, 1, 2]]
    # output: 0
    # EXPLANATION:  The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
    ,
    # example 3
    [[11, 13, 15, 17]]
    # output: 11
    # EXPLANATION:  The original array was [11,13,15,17] and it was rotated 4 times.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findMin 
from typing import *
def f_gold(nums: List[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[0] <= nums[mid]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
"-----------------"
test()

