
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]]
    # output: 7
    # EXPLANATION:  The guarded and unguarded cells are shown in red and green respectively in the above diagram. There are a total of 7 unguarded cells, so we return 7.
    ,
    # example 2
    [3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]]
    # output: 4
    # EXPLANATION:  The unguarded cells are shown in green in the above diagram. There are a total of 4 unguarded cells, so we return 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countUnguarded 
from typing import *
def f_gold(m: int, n: int, guards: List[List[int]], walls: List[List[int]]
) -> int:
    g = [[None] * n for _ in range(m)]
    for r, c in guards:
        g[r][c] = 'g'
    for r, c in walls:
        g[r][c] = 'w'
    for i, j in guards:
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i, j
            while (
                0 <= x + a < m
                and 0 <= y + b < n
                and g[x + a][y + b] != 'w'
                and g[x + a][y + b] != 'g'
            ):
                x, y = x + a, y + b
                g[x][y] = 'v'
    return sum(not v for row in g for v in row)
"-----------------"
test()

