
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 0, 3, 12]]
    # output: [1,3,12,0,0]
    ,
    # example 2
    [[0]]
    # output: [0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### moveZeroes 
from typing import *
def f_gold(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, n = 0, len(nums)
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
"-----------------"
test()

