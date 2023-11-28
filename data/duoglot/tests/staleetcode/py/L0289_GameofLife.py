
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]]
    # output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    ,
    # example 2
    [[[1, 1], [1, 0]]]
    # output: [[1,1],[1,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### gameOfLife 
from typing import *
def f_gold(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    for i in range(m):
        for j in range(n):
            cnt = sum(
                1
                for a, b in dirs
                if 0 <= i + a < m
                and 0 <= j + b < n
                and board[i + a][j + b] in (1, 2)
            )
            if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                board[i][j] = 2
            elif board[i][j] == 0 and (cnt == 3):
                board[i][j] = 3
    for i in range(m):
        for j in range(n):
            board[i][j] %= 2
"-----------------"
test()

