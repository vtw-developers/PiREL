
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: [[1,4,7],[2,5,8],[3,6,9]]
    ,
    # example 2
    [[[1, 2, 3], [4, 5, 6]]]
    # output: [[1,4],[2,5],[3,6]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### transpose 
from typing import *
def f_gold(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            res[i][j] = matrix[j][i]
    return res
"-----------------"
test()

