
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]]
    # output: 4
    # EXPLANATION:   In the beginning, you start at square 1 (at row 5, column 0). You decide to move to square 2 and must take the ladder to square 15. You then decide to move to square 17 and must take the snake to square 13. You then decide to move to square 14 and must take the ladder to square 35. You then decide to move to square 36, ending the game. This is the lowest possible number of moves to reach the last square, so return 4.
    ,
    # example 2
    [[[-1, -1], [-1, 3]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### snakesAndLadders 
from collections import deque
from typing import *
def f_gold(board: List[List[int]]) -> int:
    def get(x):
        i, j = (x - 1) // n, (x - 1) % n
        if i & 1:
            j = n - 1 - j
        return n - 1 - i, j
    n = len(board)
    q = deque([1])
    vis = {1}
    ans = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr == n * n:
                return ans
            for next in range(curr + 1, min(curr + 7, n * n + 1)):
                i, j = get(next)
                if board[i][j] != -1:
                    next = board[i][j]
                if next not in vis:
                    q.append(next)
                    vis.add(next)
        ans += 1
    return -1
"-----------------"
test()

