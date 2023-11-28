
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 4, 7, 11], 5]
    # output: 9
    # EXPLANATION: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup> missing positive integer is 9.
    ,
    # example 2
    [[1, 2, 3, 4], 2]
    # output: 6
    # EXPLANATION: The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findKthPositive 
from typing import *
def f_gold(arr: List[int], k: int) -> int:
    if arr[0] > k:
        return k
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] - mid - 1 >= k:
            right = mid
        else:
            left = mid + 1
    return arr[left - 1] + k - (arr[left - 1] - (left - 1) - 1)
"-----------------"
test()

