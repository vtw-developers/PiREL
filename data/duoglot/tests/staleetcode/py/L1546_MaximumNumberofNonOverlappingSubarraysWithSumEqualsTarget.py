
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1, 1, 1], 2]
    # output: 2
    # EXPLANATION:  There are 2 non-overlapping subarrays [<strong>1,1</strong>,1,<strong>1,1</strong>] with sum equals to target(2).
    ,
    # example 2
    [[-1, 3, 5, 1, 4, 2, -9], 6]
    # output: 2
    # EXPLANATION:  There are 3 subarrays with sum equal to 6. ([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxNonOverlapping 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    i, n = 0, len(nums)
    ans = 0
    while i < n:
        s = 0
        seen = {0}
        while i < n:
            s += nums[i]
            if s - target in seen:
                ans += 1
                break
            i += 1
            seen.add(s)
        i += 1
    return ans
"-----------------"
test()

