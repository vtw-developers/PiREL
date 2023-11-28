
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[14, 4, 18, 1, 15], 3, 15, 9]
    # output: 3
    # EXPLANATION:  3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
    ,
    # example 2
    [[8, 3, 16, 6, 12, 20], 15, 13, 11]
    # output: -1
    ,
    # example 3
    [[1, 6, 2, 14, 5, 17, 4], 16, 9, 7]
    # output: 2
    # EXPLANATION:  One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumJumps 
from collections import deque
from typing import *
def f_gold(forbidden: List[int], a: int, b: int, x: int) -> int:
    s = set(forbidden)
    q = deque([(0, 0)])
    vis = {(0, 1), (0, -1)}
    ans = 0
    while q:
        for _ in range(len(q)):
            i, dir = q.popleft()
            if i == x:
                return ans
            nxt = [(i + a, 1)]
            if dir != -1:
                nxt.append((i - b, -1))
            for j, dir in nxt:
                if 0 <= j <= 6000 and j not in s and (j, dir) not in vis:
                    vis.add((j, dir))
                    q.append((j, dir))
        ans += 1
    return -1
"-----------------"
test()

