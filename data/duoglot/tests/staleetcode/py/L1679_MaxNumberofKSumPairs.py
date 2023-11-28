
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], 5]
    # output: 2
    # EXPLANATION:  Starting with nums = [1,2,3,4]: - Remove numbers 1 and 4, then nums = [2,3] - Remove numbers 2 and 3, then nums = [] There are no more pairs that sum up to 5, hence a total of 2 operations.
    ,
    # example 2
    [[3, 1, 3, 4, 3], 6]
    # output: 1
    # EXPLANATION:  Starting with nums = [3,1,3,4,3]: - Remove the first two 3's, then nums = [1,4,3] There are no more pairs that sum up to 6, hence a total of 1 operation.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxOperations 
from typing import *
def f_gold(nums: List[int], k: int) -> int:
    nums.sort()
    l, r, ans = 0, len(nums) - 1, 0
    while l < r:
        s = nums[l] + nums[r]
        if s == k:
            ans += 1
            l, r = l + 1, r - 1
        elif s > k:
            r -= 1
        else:
            l += 1
    return ans
"-----------------"
test()

