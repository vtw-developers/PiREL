
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 8], [4, 7]]
    # output: [[3,0],         [1,7]]
    # EXPLANATION:   0<sup>th</sup> row: 3 + 0 = 3 == rowSum[0] 1<sup>st</sup> row: 1 + 7 = 8 == rowSum[1] 0<sup>th</sup> column: 3 + 1 = 4 == colSum[0] 1<sup>st</sup> column: 0 + 7 = 7 == colSum[1] The row and column sums match, and all matrix elements are non-negative. Another possible matrix is: [[1,2],                              [3,5]]
    ,
    # example 2
    [[5, 7, 10], [8, 6, 8]]
    # output: [[0,5,0],         [6,1,0],         [2,0,8]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### restoreMatrix 
from typing import *
def f_gold(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    m, n = len(rowSum), len(colSum)
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            x = min(rowSum[i], colSum[j])
            ans[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
    return ans
"-----------------"
test()

