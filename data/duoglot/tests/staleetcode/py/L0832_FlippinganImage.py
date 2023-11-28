
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 0], [1, 0, 1], [0, 0, 0]]]
    # output: [[1,0,0],[0,1,0],[1,1,1]]
    # EXPLANATION:  First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
    ,
    # example 2
    [[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]]
    # output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    # EXPLANATION:  First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### flipAndInvertImage 
from typing import *
def f_gold(A: List[List[int]]) -> List[List[int]]:
    m, n = len(A), len(A[0])
    for i in range(m):
        p, q = 0, n - 1
        while p < q:
            t = A[i][p] ^ 1
            A[i][p] = A[i][q] ^ 1
            A[i][q] = t
            p += 1
            q -= 1
        if p == q:
            A[i][p] ^= 1
    return A
"-----------------"
test()

