
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 3, 5]
    # output: 3
    # EXPLANATION:  The 5<sup>th</sup> smallest number is 3.
    ,
    # example 2
    [2, 3, 6]
    # output: 6
    # EXPLANATION:  The 6<sup>th</sup> smallest number is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findKthNumber 
from typing import *
def f_gold(m: int, n: int, k: int) -> int:
    left, right = 1, m * n
    while left < right:
        mid = (left + right) >> 1
        cnt = 0
        for i in range(1, m + 1):
            cnt += min(mid // i, n)
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

