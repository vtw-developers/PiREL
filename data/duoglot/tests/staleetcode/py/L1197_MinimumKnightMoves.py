
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 1]
    # output: 1
    # EXPLANATION: [0, 0]   [2, 1]
    ,
    # example 2
    [5, 5]
    # output: 4
    # EXPLANATION: [0, 0]   [2, 1]   [4, 2]   [3, 4]   [5, 5]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minKnightMoves 
from collections import deque
from typing import *
def f_gold(x: int, y: int) -> int:
    q = deque([(0, 0)])
    ans = 0
    vis = {(0, 0)}
    dirs = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == (x, y):
                return ans
            for a, b in dirs:
                c, d = i + a, j + b
                if (c, d) not in vis:
                    vis.add((c, d))
                    q.append((c, d))
        ans += 1
    return -1
"-----------------"
test()

