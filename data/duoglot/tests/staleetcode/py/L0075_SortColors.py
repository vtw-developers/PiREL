
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 0, 2, 1, 1, 0]]
    # output: [0,0,1,1,2,2]
    ,
    # example 2
    [[2, 0, 1]]
    # output: [0,1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortColors 
from typing import *
def f_gold(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j = -1, len(nums)
    cur = 0
    while cur < j:
        if nums[cur] == 0:
            i += 1
            nums[cur], nums[i] = nums[i], nums[cur]
            cur += 1
        elif nums[cur] == 1:
            cur += 1
        else:
            j -= 1
            nums[cur], nums[j] = nums[j], nums[cur]
"-----------------"
test()

