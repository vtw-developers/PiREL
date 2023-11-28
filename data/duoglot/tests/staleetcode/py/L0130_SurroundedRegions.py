
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]]
    # output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    # EXPLANATION:  Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
    ,
    # example 2
    [[["X"]]]
    # output: [["X"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### solve 
from typing import *
def f_gold(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def dfs(i, j):
        board[i][j] = '.'
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                dfs(x, y)
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and (
                i == 0 or i == m - 1 or j == 0 or j == n - 1
            ):
                dfs(i, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '.':
                board[i][j] = 'O'
"-----------------"
test()

