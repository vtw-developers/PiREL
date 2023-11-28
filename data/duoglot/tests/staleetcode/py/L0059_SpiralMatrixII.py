
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: [[1,2,3],[8,9,4],[7,6,5]]
    ,
    # example 2
    [1]
    # output: [[1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### generateMatrix 
from typing import *
def f_gold(n: int) -> List[List[int]]:
    res = [[0] * n for _ in range(n)]
    num = 1
    m1, m2 = 0, n - 1
    while m1 < m2:
        for j in range(m1, m2):
            res[m1][j] = num
            num += 1
        for i in range(m1, m2):
            res[i][m2] = num
            num += 1
        for j in range(m2, m1, -1):
            res[m2][j] = num
            num += 1
        for i in range(m2, m1, -1):
            res[i][m1] = num
            num += 1
        m1 += 1
        m2 -= 1
    if m1 == m2:
        res[m1][m1] = num
    return res
"-----------------"
test()

