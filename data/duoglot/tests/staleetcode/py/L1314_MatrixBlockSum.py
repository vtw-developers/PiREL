
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1]
    # output: [[12,21,16],[27,45,33],[24,39,28]]
    ,
    # example 2
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2]
    # output: [[45,45,45],[45,45,45],[45,45,45]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### matrixBlockSum 
from typing import *
def f_gold(mat: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    pre = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            pre[i][j] = (
                pre[i - 1][j]
                + pre[i][j - 1]
                - pre[i - 1][j - 1]
                + mat[i - 1][j - 1]
            )
    def get(i, j):
        i = max(min(m, i), 0)
        j = max(min(n, j), 0)
        return pre[i][j]
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = (
                get(i + k + 1, j + k + 1)
                - get(i + k + 1, j - k)
                - get(i - k, j + k + 1)
                + get(i - k, j - k)
            )
    return ans
"-----------------"
test()

