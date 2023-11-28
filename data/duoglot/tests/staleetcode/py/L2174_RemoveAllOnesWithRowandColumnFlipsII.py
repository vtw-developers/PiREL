
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 1], [1, 1, 1], [0, 1, 0]]]
    # output: 2
    # EXPLANATION:  In the first operation, change all cell values of row 1 and column 1 to zero. In the second operation, change all cell values of row 0 and column 0 to zero.
    ,
    # example 2
    [[[0, 1, 0], [1, 0, 1], [0, 1, 0]]]
    # output: 2
    # EXPLANATION:  In the first operation, change all cell values of row 1 and column 0 to zero. In the second operation, change all cell values of row 2 and column 1 to zero. Note that we cannot perform an operation using row 1 and column 1 because grid[1][1] != 1.
    ,
    # example 3
    [[[0, 0], [0, 0]]]
    # output: 0
    # EXPLANATION:  There are no 1's to remove so return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeOnes 
from collections import deque
from typing import *
def f_gold(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    state = sum(1 << (i * n + j) for i in range(m) for j in range(n) if grid[i][j])
    q = deque([state])
    vis = {state}
    ans = 0
    while q:
        for _ in range(len(q)):
            state = q.popleft()
            if state == 0:
                return ans
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        continue
                    nxt = state
                    for r in range(m):
                        nxt &= ~(1 << (r * n + j))
                    for c in range(n):
                        nxt &= ~(1 << (i * n + c))
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
        ans += 1
    return -1
"-----------------"
test()

