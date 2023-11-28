
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: [[7,4,1],[8,5,2],[9,6,3]]
    ,
    # example 2
    [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]]
    # output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### rotate 
from typing import *
def f_gold(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    s, n = 0, len(matrix)
    while s < (n >> 1):
        e = n - s - 1
        for i in range(s, e):
            t = matrix[i][e]
            matrix[i][e] = matrix[s][i]
            matrix[s][i] = matrix[n - i - 1][s]
            matrix[n - i - 1][s] = matrix[e][n - i - 1]
            matrix[e][n - i - 1] = t
        s += 1
"-----------------"
test()

