
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [0, 1]]]
    # output: 3
    # EXPLANATION:  One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
    ,
    # example 2
    [[[0]]]
    # output: 0
    # EXPLANATION:  Given matrix is a zero matrix. We do not need to change it.
    ,
    # example 3
    [[[1, 0, 0], [1, 0, 0]]]
    # output: -1
    # EXPLANATION:  Given matrix cannot be a zero matrix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minFlips 
from collections import deque
from typing import *
def f_gold(mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    state = sum(1 << (i * n + j) for i in range(m) for j in range(n) if mat[i][j])
    q = deque([state])
    vis = {state}
    ans = 0
    dirs = [0, -1, 0, 1, 0, 0]
    while q:
        for _ in range(len(q)):
            state = q.popleft()
            if state == 0:
                return ans
            for i in range(m):
                for j in range(n):
                    nxt = state
                    for k in range(5):
                        x, y = i + dirs[k], j + dirs[k + 1]
                        if not 0 <= x < m or not 0 <= y < n:
                            continue
                        if nxt & (1 << (x * n + y)):
                            nxt -= 1 << (x * n + y)
                        else:
                            nxt |= 1 << (x * n + y)
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
        ans += 1
    return -1
"-----------------"
test()

