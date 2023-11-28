
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]]
    # output: [[1,0,1],[0,0,0],[1,0,1]]
    ,
    # example 2
    [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]]
    # output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### setZeroes 
from typing import *
def f_gold(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    zero_rows = [False] * m
    zero_cols = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows[i] = zero_cols[j] = True
    for i in range(m):
        for j in range(n):
            if zero_rows[i] or zero_cols[j]:
                matrix[i][j] = 0
"-----------------"
test()

