
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"]
    # output: true
    ,
    # example 2
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"]
    # output: true
    ,
    # example 3
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### exist 
from typing import *
def f_gold(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, cur):
        if cur == len(word):
            return True
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or board[i][j] == '0'
            or word[cur] != board[i][j]
        ):
            return False
        t = board[i][j]
        board[i][j] = '0'
        for a, b in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            x, y = i + a, j + b
            if dfs(x, y, cur + 1):
                return True
        board[i][j] = t
        return False
    m, n = len(board), len(board[0])
    return any(dfs(i, j, 0) for i in range(m) for j in range(n))
"-----------------"
test()

