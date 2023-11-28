
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 4]]
    # output: [2,4,3,1]
    # EXPLANATION:  The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
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
### sortArrayByParity 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] & 1:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    return nums
"-----------------"
test()

