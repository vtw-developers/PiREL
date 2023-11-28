
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]]
    # output: [1,5]
    # EXPLANATION: Only 1 and 5 appeared in the three arrays.
    ,
    # example 2
    [[197, 418, 523, 876, 1356], [501, 880, 1593, 1710, 1870], [521, 682, 1337, 1395, 1764]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### arraysIntersection 
from typing import *
def f_gold(arr1: List[int], arr2: List[int], arr3: List[int]
) -> List[int]:
    def find(arr, val):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] >= val:
                right = mid
            else:
                left = mid + 1
        return arr[left] == val
    res = []
    for num in arr1:
        if find(arr2, num) and find(arr3, num):
            res.append(num)
    return res
"-----------------"
test()

