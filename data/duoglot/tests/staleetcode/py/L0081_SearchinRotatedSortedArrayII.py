
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 6, 0, 0, 1, 2], 0]
    # output: true
    ,
    # example 2
    [[2, 5, 6, 0, 0, 1, 2], 3]
    # output: false
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
def f_gold(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            return True
        if nums[mid] < nums[r] or nums[mid] < nums[l]:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        elif nums[mid] > nums[l] or nums[mid] > nums[r]:
            if target < nums[mid] and target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            r -= 1
    return False
"-----------------"
test()

