
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: [1,2,3,6,9,8,7,4,5]
    ,
    # example 2
    [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    # output: [1,2,3,4,8,12,11,10,9,5,6,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### spiralOrder 
from typing import *
def f_gold(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    ans = []
    top, bottom, left, right = 0, m - 1, 0, n - 1
    while left <= right and top <= bottom:
        ans.extend([matrix[top][j] for j in range(left, right + 1)])
        ans.extend([matrix[i][right] for i in range(top + 1, bottom + 1)])
        if left < right and top < bottom:
            ans.extend([matrix[bottom][j] for j in range(right - 1, left - 1, -1)])
            ans.extend([matrix[i][left] for i in range(bottom - 1, top, -1)])
        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
    return ans
"-----------------"
test()

