
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 2, 5, 10, 8], 2]
    # output: 18
    # EXPLANATION:  There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
    ,
    # example 2
    [[1, 2, 3, 4, 5], 2]
    # output: 9
    ,
    # example 3
    [[1, 4, 4], 3]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### splitArray 
from typing import *
def f_gold(nums: List[int], m: int) -> int:
    def check(x):
        s, cnt = 0, 1
        for num in nums:
            if s + num > x:
                cnt += 1
                s = num
            else:
                s += num
        return cnt <= m
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) >> 1
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

