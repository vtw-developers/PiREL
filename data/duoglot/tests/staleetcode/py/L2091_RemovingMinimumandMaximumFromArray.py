
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 10, 7, 5, 4, 1, 8, 6]]
    # output: 5
    # EXPLANATION:   The minimum element in the array is nums[5], which is 1. The maximum element in the array is nums[1], which is 10. We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back. This results in 2 + 3 = 5 deletions, which is the minimum number possible.
    ,
    # example 2
    [[0, -4, 19, 1, 8, -2, -3, 5]]
    # output: 3
    # EXPLANATION:   The minimum element in the array is nums[1], which is -4. The maximum element in the array is nums[2], which is 19. We can remove both the minimum and maximum by removing 3 elements from the front. This results in only 3 deletions, which is the minimum number possible.
    ,
    # example 3
    [[101]]
    # output: 1
    # EXPLANATION:    There is only one element in the array, which makes it both the minimum and maximum element. We can remove it with 1 deletion.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumDeletions 
from typing import *
def f_gold(nums: List[int]) -> int:
    mi = mx = 0
    for i, num in enumerate(nums):
        if num < nums[mi]:
            mi = i
        if num > nums[mx]:
            mx = i
    if mi > mx:
        mi, mx = mx, mi
    return min(mx + 1, len(nums) - mi, mi + 1 + len(nums) - mx)
"-----------------"
test()

