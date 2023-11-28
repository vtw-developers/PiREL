
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]]
    # output: 39
    # EXPLANATION:  0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
    ,
    # example 2
    [[[0]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### matrixScore 
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if grid[i][0] == 0:
            for j in range(n):
                grid[i][j] ^= 1
    res = 0
    for j in range(n):
        cnt = 0
        for i in range(m):
            cnt += grid[i][j]
        res += max(cnt, m - cnt) * (1 << (n - j - 1))
    return res
"-----------------"
test()

