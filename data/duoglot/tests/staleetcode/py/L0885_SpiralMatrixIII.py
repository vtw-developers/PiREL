
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 4, 0, 0]
    # output: [[0,0],[0,1],[0,2],[0,3]]
    ,
    # example 2
    [5, 6, 1, 4]
    # output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### spiralMatrixIII 
from typing import *
def f_gold(rows: int, cols: int, rStart: int, cStart: int
) -> List[List[int]]:
    ans = [[rStart, cStart]]
    if rows * cols == 1:
        return ans
    k = 1
    while True:
        for dr, dc, dk in [[0, 1, k], [1, 0, k], [0, -1, k + 1], [-1, 0, k + 1]]:
            for _ in range(dk):
                rStart += dr
                cStart += dc
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    if len(ans) == rows * cols:
                        return ans
        k += 2
"-----------------"
test()

