
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 4, 2, 3], 5]
    # output: 2
    # EXPLANATION:  The optimal solution is to remove the last two elements to reduce x to zero.
    ,
    # example 2
    [[5, 6, 7, 8, 9], 4]
    # output: -1
    ,
    # example 3
    [[3, 2, 20, 1, 1, 3], 10]
    # output: 5
    # EXPLANATION:  The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
import math
from math import inf
from typing import *
def f_gold(nums: List[int], x: int) -> int:
    x = sum(nums) - x
    n = len(nums)
    s = 0
    seen = {0: -1}
    ans = float('inf')
    for i, v in enumerate(nums):
        s += v
        if s not in seen:
            seen[s] = i
        if s - x in seen:
            j = seen[s - x]
            ans = min(ans, n - (i - j))
    return -1 if ans == float('inf') else ans
"-----------------"
test()

