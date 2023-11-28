
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-2, 0, 1, 3], 2]
    # output: 2
    # EXPLANATION:  Because there are two triplets which sums are less than 2: [-2,0,1] [-2,0,3]
    ,
    # example 2
    [[], 0]
    # output: 0
    ,
    # example 3
    [[0], 0]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### threeSumSmaller 
from typing import *
def f_gold(nums: List[int], target: int) -> int:
    nums.sort()
    ans, n = 0, len(nums)
    for i in range(n):
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s >= target:
                k -= 1
            else:
                ans += k - j
                j += 1
    return ans
"-----------------"
test()

