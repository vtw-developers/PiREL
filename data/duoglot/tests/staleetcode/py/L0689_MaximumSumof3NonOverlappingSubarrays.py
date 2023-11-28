
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1, 2, 6, 7, 5, 1], 2]
    # output: [0,3,5]
    # EXPLANATION:  Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5]. We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
    ,
    # example 2
    [[1, 2, 1, 2, 1, 2, 1, 2, 1], 2]
    # output: [0,2,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSumOfThreeSubarrays 
from typing import *
def f_gold(nums: List[int], k: int) -> List[int]:
    s = s1 = s2 = s3 = 0
    mx1 = mx12 = 0
    idx1, idx12 = 0, ()
    ans = []
    for i in range(k * 2, len(nums)):
        s1 += nums[i - k * 2]
        s2 += nums[i - k]
        s3 += nums[i]
        if i >= k * 3 - 1:
            if s1 > mx1:
                mx1 = s1
                idx1 = i - k * 3 + 1
            if mx1 + s2 > mx12:
                mx12 = mx1 + s2
                idx12 = (idx1, i - k * 2 + 1)
            if mx12 + s3 > s:
                s = mx12 + s3
                ans = [*idx12, i - k + 1]
            s1 -= nums[i - k * 3 + 1]
            s2 -= nums[i - k * 2 + 1]
            s3 -= nums[i - k + 1]
    return ans
"-----------------"
test()

