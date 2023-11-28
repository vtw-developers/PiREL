
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3]
    # output: true
    ,
    # example 2
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### searchMatrix 
from typing import *
def f_gold(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left < right:
        mid = (left + right) >> 1
        x, y = divmod(mid, n)
        if matrix[x][y] >= target:
            right = mid
        else:
            left = mid + 1
    return matrix[left // n][left % n] == target
"-----------------"
test()

