
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: [1,2,4,7,5,3,6,8,9]
    ,
    # example 2
    [[[1, 2], [3, 4]]]
    # output: [1,2,3,4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findDiagonalOrder 
from typing import *
def f_gold(mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    ans = []
    for k in range(m + n - 1):
        t = []
        i = 0 if k < n else k - n + 1
        j = k if k < n else n - 1
        while i < m and j >= 0:
            t.append(mat[i][j])
            i += 1
            j -= 1
        if k % 2 == 0:
            t = t[::-1]
        ans.extend(t)
    return ans
"-----------------"
test()

