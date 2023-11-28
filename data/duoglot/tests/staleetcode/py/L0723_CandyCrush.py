
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414], [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]]
    # output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
    ,
    # example 2
    [[[1, 3, 5, 5, 2], [3, 4, 3, 3, 1], [3, 2, 4, 5, 2], [2, 4, 4, 5, 5], [1, 4, 4, 1, 1]]]
    # output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### candyCrush 
from typing import *
def f_gold(board: List[List[int]]) -> List[List[int]]:
    m, n = len(board), len(board[0])
    run = True
    while run:
        run = False
        for i in range(m):
            for j in range(n - 2):
                if (
                    board[i][j] != 0
                    and abs(board[i][j]) == abs(board[i][j + 1])
                    and abs(board[i][j]) == abs(board[i][j + 2])
                ):
                    run = True
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(
                        board[i][j]
                    )
        for j in range(n):
            for i in range(m - 2):
                if (
                    board[i][j] != 0
                    and abs(board[i][j]) == abs(board[i + 1][j])
                    and abs(board[i][j]) == abs(board[i + 2][j])
                ):
                    run = True
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(
                        board[i][j]
                    )
        if run:
            for j in range(n):
                curr = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[curr][j] = board[i][j]
                        curr -= 1
                while curr > -1:
                    board[curr][j] = 0
                    curr -= 1
    return board
"-----------------"
test()

