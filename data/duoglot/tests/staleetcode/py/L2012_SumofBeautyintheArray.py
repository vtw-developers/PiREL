
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 2
    # EXPLANATION:  For each index i in the range 1 <= i <= 1: - The beauty of nums[1] equals 2.
    ,
    # example 2
    [[2, 4, 6, 4]]
    # output: 1
    # EXPLANATION:  For each index i in the range 1 <= i <= 2: - The beauty of nums[1] equals 1. - The beauty of nums[2] equals 0.
    ,
    # example 3
    [[3, 2, 1]]
    # output: 0
    # EXPLANATION:  For each index i in the range 1 <= i <= 1: - The beauty of nums[1] equals 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumOfBeauties 
from typing import *
def f_gold(nums: List[int]) -> int:
    n = len(nums)
    lmx = [0] * n
    for i in range(1, n):
        lmx[i] = max(lmx[i - 1], nums[i - 1])
    rmi = [100001] * n
    for i in range(n - 2, -1, -1):
        rmi[i] = min(rmi[i + 1], nums[i + 1])
    ans = 0
    for i in range(1, n - 1):
        if lmx[i] < nums[i] < rmi[i]:
            ans += 2
        elif nums[i - 1] < nums[i] < nums[i + 1]:
            ans += 1
    return ans
"-----------------"
test()

