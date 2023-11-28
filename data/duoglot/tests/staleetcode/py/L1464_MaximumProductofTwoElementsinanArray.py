
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 4, 5, 2]]
    # output: 12
    # EXPLANATION:  If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
    ,
    # example 2
    [[1, 5, 4, 5]]
    # output: 16
    # EXPLANATION:  Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
    ,
    # example 3
    [[3, 7]]
    # output: 12
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxProduct 
from typing import *
def f_gold(nums: List[int]) -> int:
    i = 0 if nums[0] > nums[1] else 1
    j = 1 - i
    for k in range(2, len(nums)):
        if nums[k] > nums[i]:
            j = k
            i, j = j, i
        elif nums[k] > nums[j]:
            j = k
    return (nums[i] - 1) * (nums[j] - 1)
"-----------------"
test()

