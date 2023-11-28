
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]]
    # output: 3
    # EXPLANATION:  In this example, the rook is attacking all the pawns.
    ,
    # example 2
    [[[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."], [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."], [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]]
    # output: 0
    # EXPLANATION:  The bishops are blocking the rook from attacking any of the pawns.
    ,
    # example 3
    [[[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]]
    # output: 3
    # EXPLANATION:  The rook is attacking the pawns at positions b5, d6, and f5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numRookCaptures 
from typing import *
def f_gold(board: List[List[str]]) -> int:
    x, y, n = 0, 0, 8
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'R':
                x, y = i, j
                break
    ans = 0
    for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        i, j = x, y
        while 0 <= i + a < n and 0 <= j + b < n and board[i + a][j + b] != 'B':
            i, j = i + a, j + b
            if board[i][j] == 'p':
                ans += 1
                break
    return ans
"-----------------"
test()

