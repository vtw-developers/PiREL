
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 6, 7, 11], 8]
    # output: 4
    ,
    # example 2
    [[30, 11, 23, 4, 20], 5]
    # output: 30
    ,
    # example 3
    [[30, 11, 23, 4, 20], 6]
    # output: 23
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minEatingSpeed 
from typing import *
def f_gold(piles: List[int], h: int) -> int:
    left, right = 1, int(1e9)
    while left < right:
        mid = (left + right) >> 1
        s = sum((x + mid - 1) // mid for x in piles)
        if s <= h:
            right = mid
        else:
            left = mid + 1
    return left
"-----------------"
test()

