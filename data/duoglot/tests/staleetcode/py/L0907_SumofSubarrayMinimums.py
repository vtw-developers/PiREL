
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 4]]
    # output: 17
    # EXPLANATION:   Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].  Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1. Sum is 17.
    ,
    # example 2
    [[11, 81, 94, 43, 3]]
    # output: 444
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### sumSubarrayMins 
from typing import *
def f_gold(arr: List[int]) -> int:
    n = len(arr)
    left = [-1] * n
    right = [n] * n
    stk = []
    for i, v in enumerate(arr):
        while stk and arr[stk[-1]] >= v:
            stk.pop()
        if stk:
            left[i] = stk[-1]
        stk.append(i)
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] > arr[i]:
            stk.pop()
        if stk:
            right[i] = stk[-1]
        stk.append(i)
    mod = int(1e9) + 7
    return sum((i - left[i]) * (right[i] - i) * v for i, v in enumerate(arr)) % mod
"-----------------"
test()

