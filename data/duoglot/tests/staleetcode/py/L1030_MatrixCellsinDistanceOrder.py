
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2, 0, 0]
    # output: [[0,0],[0,1]]
    # EXPLANATION:  The distances from (0, 0) to other cells are: [0,1]
    ,
    # example 2
    [2, 2, 0, 1]
    # output: [[0,1],[0,0],[1,1],[1,0]]
    # EXPLANATION:  The distances from (0, 1) to other cells are: [0,1,1,2] The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
    ,
    # example 3
    [2, 3, 1, 2]
    # output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
    # EXPLANATION:  The distances from (1, 2) to other cells are: [0,1,1,2,2,3] There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### allCellsDistOrder 
from collections import deque
from typing import *
def f_gold(rows: int, cols: int, rCenter: int, cCenter: int
) -> List[List[int]]:
    q = deque([(rCenter, cCenter)])
    vis = [[False] * cols for _ in range(rows)]
    vis[rCenter][cCenter] = True
    ans = []
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            ans.append([i, j])
            for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                x, y = i + a, j + b
                if 0 <= x < rows and 0 <= y < cols and not vis[x][y]:
                    q.append((x, y))
                    vis[x][y] = True
    return ans
"-----------------"
test()

