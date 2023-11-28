
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 2, 1, 5, 3, 4]]
    # output: [0,1,2,4,5,3]<strong>
    # EXPLANATION: </strong> The array ans is built as follows:  ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]     = [0,1,2,4,5,3]
    ,
    # example 2
    [[5, 0, 1, 2, 3, 4]]
    # output: [4,5,0,1,2,3]
    # EXPLANATION:  The array ans is built as follows: ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]     = [4,5,0,1,2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### buildArray 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    return [nums[num] for num in nums]
"-----------------"
test()

