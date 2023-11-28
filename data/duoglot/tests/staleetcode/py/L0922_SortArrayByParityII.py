
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 5, 7]]
    # output: [4,5,2,7]
    # EXPLANATION:  [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    ,
    # example 2
    [[2, 3]]
    # output: [2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sortArrayByParityII 
from typing import *
def f_gold(nums: List[int]) -> List[int]:
    n, j = len(nums), 1
    for i in range(0, n, 2):
        if (nums[i] & 1) == 1:
            while (nums[j] & 1) == 1:
                j += 2
            nums[i], nums[j] = nums[j], nums[i]
    return nums
"-----------------"
test()

