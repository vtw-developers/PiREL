
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 6, 1, 0]]
    # output: 1
    # EXPLANATION:  6 is the largest integer. For every other number in the array x, 6 is at least twice as big as x. The index of value 6 is 1, so we return 1.
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: -1
    # EXPLANATION:  4 is less than twice the value of 3, so we return -1.
    ,
    # example 3
    [[1]]
    # output: 0
    # EXPLANATION:  1 is trivially at least twice the value as any other number because there are no other numbers.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### dominantIndex 
from typing import *
def f_gold(nums: List[int]) -> int:
    mx = mid = 0
    ans = -1
    for i, v in enumerate(nums):
        if v > mx:
            mid, mx = mx, v
            ans = i
        elif v > mid:
            mid = v
    return ans if mx >= 2 * mid else -1
"-----------------"
test()

