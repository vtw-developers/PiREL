
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [1, 0]], [[1, 0], [0, 1]]]
    # output: true
    # EXPLANATION: We can rotate mat 90 degrees clockwise to make mat equal target.
    ,
    # example 2
    [[[0, 1], [1, 1]], [[1, 0], [0, 1]]]
    # output: false
    # EXPLANATION:  It is impossible to make mat equal to target by rotating mat.
    ,
    # example 3
    [[[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]]
    # output: true
    # EXPLANATION: We can rotate mat 90 degrees clockwise two times to make mat equal target.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findRotation 
from typing import *
def f_gold(mat: List[List[int]], target: List[List[int]]) -> bool:
    def rotate(matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                t = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = t
    for _ in range(4):
        if mat == target:
            return True
        rotate(mat)
    return False
"-----------------"
test()

