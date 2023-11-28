
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], 4, 3]
    # output: [1,2,3,4]
    ,
    # example 2
    [[1, 2, 3, 4, 5], 4, -1]
    # output: [1,2,3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findClosestElements 
from typing import *
def f_gold(arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) >> 1
        if x - arr[mid] <= arr[mid + k] - x:
            right = mid
        else:
            left = mid + 1
    return arr[left : left + k]
"-----------------"
test()

