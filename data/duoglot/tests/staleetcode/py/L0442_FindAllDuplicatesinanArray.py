
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 7, 8, 2, 3, 1]]
    # output: [2,3]
    ,
    # example 2
    [[1, 1, 2]]
    # output: [1]
    ,
    # example 3
    [[1]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDuplicates 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        while nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return [v for i, v in enumerate(nums) if v != i + 1]
"-----------------"
test()

