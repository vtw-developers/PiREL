
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]]
    # output: 2
    ,
    # example 2
    [[["."]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countBattleships 
from typing import *
def f_gold(board: List[List[str]]) -> int:
    m, n = len(board), len(board[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                continue
            if i > 0 and board[i - 1][j] == 'X':
                continue
            if j > 0 and board[i][j - 1] == 'X':
                continue
            ans += 1
    return ans
"-----------------"
test()

