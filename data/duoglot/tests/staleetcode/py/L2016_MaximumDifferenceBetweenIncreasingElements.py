
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 1, 5, 4]]
    # output: 4
    # EXPLANATION:  The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4. Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
    ,
    # example 2
    [[9, 4, 3, 2]]
    # output: -1
    # EXPLANATION:  There is no i and j such that i < j and nums[i] < nums[j].
    ,
    # example 3
    [[1, 5, 2, 10]]
    # output: 9
    # EXPLANATION:  The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumDifference 
from typing import *
def f_gold(nums: List[int]) -> int:
    mi = nums[0]
    ans, n = -1, len(nums)
    for i in range(1, n):
        if nums[i] > mi:
            ans = max(ans, nums[i] - mi)
        else:
            mi = nums[i]
    return ans
"-----------------"
test()

