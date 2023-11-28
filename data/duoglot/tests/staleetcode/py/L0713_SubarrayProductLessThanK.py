
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 5, 2, 6], 100]
    # output: 8
    # EXPLANATION:  The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6] Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
    ,
    # example 2
    [[1, 2, 3], 0]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSubarrayProductLessThanK 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    ans, s, j = 0, 1, 0
    for i, v in enumerate(nums):
        s *= v
        while j <= i and s >= k:
            s //= nums[j]
            j += 1
        ans += i - j + 1
    return ans
"-----------------"
test()

