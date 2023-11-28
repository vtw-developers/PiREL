
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5]]
    # output: 8
    # EXPLANATION:  The above diagram depicts the process from which we obtain the triangular sum of the array.
    ,
    # example 2
    [[5]]
    # output: 5
    # EXPLANATION:  Since there is only one element in nums, the triangular sum is the value of that element itself.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### triangularSum 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            nums[j] = (nums[j] + nums[j + 1]) % 10
    return nums[0]
"-----------------"
test()

