
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 3, [[0, 1], [1, 1]]]
    # output: 6
    # EXPLANATION:  Initial matrix = [[0,0,0],[0,0,0]]. After applying first increment it becomes [[1,2,1],[0,1,0]]. The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
    ,
    # example 2
    [2, 2, [[1, 1], [0, 0]]]
    # output: 0
    # EXPLANATION:  Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### oddCells 
from typing import *
def f_gold(m: int, n: int, indices: List[List[int]]) -> int:
    g = [[0] * n for _ in range(m)]
    for r, c in indices:
        for i in range(m):
            g[i][c] += 1
        for j in range(n):
            g[r][j] += 1
    return sum(g[i][j] % 2 for i in range(m) for j in range(n))
"-----------------"
test()

