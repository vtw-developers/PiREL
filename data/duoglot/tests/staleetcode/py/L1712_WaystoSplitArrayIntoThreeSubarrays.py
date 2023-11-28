
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 1]]
    # output: 1
    # EXPLANATION:  The only good way to split nums is [1] [1] [1].
    ,
    # example 2
    [[1, 2, 2, 2, 5, 0]]
    # output: 3
    # EXPLANATION:  There are three good ways of splitting nums:  [1] [2] [2,2,5,0]  [1] [2,2] [2,5,0]  [1,2] [2,2] [5,0]
    ,
    # example 3
    [[3, 2, 1]]
    # output: 0
    # EXPLANATION:  There is no good way to split nums.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### waysToSplit 
from typing import *
def f_gold(nums: List[int]) -> int:
    mod = 1e9 + 7
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + nums[i - 1]
    ans = 0
    for i in range(1, n - 1):
        if pre[i] * 3 > pre[n]:
            break
        left, right = i + 1, n - 1
        while left < right:
            mid = (left + right + 1) >> 1
            if pre[mid] - pre[i] <= pre[n] - pre[mid]:
                left = mid
            else:
                right = mid - 1
        mid_right = left
        left, right = i + 1, n - 1
        while left < right:
            mid = (left + right) >> 1
            if pre[mid] - pre[i] >= pre[i]:
                right = mid
            else:
                left = mid + 1
        ans += (mid_right - left + 1) % mod
    return int(ans % mod)
"-----------------"
test()

