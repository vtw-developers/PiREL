
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 7, 8, 2, 3, 1]]
    # output: [5,6]
    ,
    # example 2
    [[1, 1]]
    # output: [2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDisappearedNumbers 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] *= -1
    return [i + 1 for i, v in enumerate(nums) if v > 0]
"-----------------"
test()

