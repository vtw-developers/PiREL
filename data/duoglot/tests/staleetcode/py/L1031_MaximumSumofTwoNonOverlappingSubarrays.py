
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2]
    # output: 20
    # EXPLANATION:  One choice of subarrays is [9] with length 1, and [6,5] with length 2.
    ,
    # example 2
    [[3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2]
    # output: 29
    # EXPLANATION:  One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
    ,
    # example 3
    [[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3]
    # output: 31
    # EXPLANATION:  One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSumTwoNoOverlap 
from typing import *
def f_gold(nums: List[int], firstLen: int, secondLen: int) -> int:
    n = len(nums)
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + nums[i - 1]
    ans1, ans2, fm, sm = 0, 0, 0, 0
    for i in range(n - firstLen - secondLen + 1):
        fm = max(fm, s[i + firstLen] - s[i])
        ans1 = max(fm + s[i + firstLen + secondLen] - s[i + firstLen], ans1)
    for i in range(n - firstLen - secondLen + 1):
        sm = max(sm, s[i + secondLen] - s[i])
        ans2 = max(sm + s[i + firstLen + secondLen] - s[i + secondLen], ans2)
    return max(ans1, ans2)
"-----------------"
test()

