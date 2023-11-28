
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1]]
    # output: false
    ,
    # example 2
    [[3, 5, 5]]
    # output: false
    ,
    # example 3
    [[0, 3, 2, 1]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validMountainArray 
from typing import *
def f_gold(arr: List[int]) -> bool:
    n = len(arr)
    if n < 3:
        return False
    l, r = 0, n - 1
    while l + 1 < n - 1 and arr[l] < arr[l + 1]:
        l += 1
    while r - 1 > 0 and arr[r] < arr[r - 1]:
        r -= 1
    return l == r
"-----------------"
test()

