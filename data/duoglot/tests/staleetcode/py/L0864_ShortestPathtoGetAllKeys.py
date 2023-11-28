
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["@.a..", "###.#", "b.A.B"]]
    # output: 8
    # EXPLANATION:  Note that the goal is to obtain all the keys not to open all the locks.
    ,
    # example 2
    [["@..aA", "..B#.", "....b"]]
    # output: 6
    ,
    # example 3
    [["@Aa"]]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestPathAllKeys 
from collections import deque
from typing import *
def f_gold(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    cnt, start = 0, None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            cnt += v.islower()
            if v == '@':
                start = (i, j)
    q = deque([(start[0], start[1], 0)])
    dirs = [-1, 0, 1, 0, -1]
    ans = 0
    mask = (1 << cnt) - 1
    vis = {(*start, 0)}
    while q:
        for _ in range(len(q)):
            i, j, state = q.popleft()
            if state == mask:
                return ans
            for k in range(4):
                nxt = state
                x, y = i + dirs[k], j + dirs[k + 1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    if (
                        grid[x][y].isupper()
                        and (nxt & (1 << (ord(grid[x][y]) - ord('A')))) == 0
                    ):
                        continue
                    if grid[x][y].islower():
                        nxt |= 1 << (ord(grid[x][y]) - ord('a'))
                    if (x, y, nxt) not in vis:
                        q.append((x, y, nxt))
                        vis.add((x, y, nxt))
        ans += 1
    return -1
"-----------------"
test()

