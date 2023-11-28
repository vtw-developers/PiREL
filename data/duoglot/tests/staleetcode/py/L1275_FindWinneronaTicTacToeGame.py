
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]]
    # output: "A"
    # EXPLANATION:  A wins, they always play first.
    ,
    # example 2
    [[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]]
    # output: "B"
    # EXPLANATION:  B wins.
    ,
    # example 3
    [[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]]
    # output: "Draw"
    # EXPLANATION:  The game ends in a draw since there are no moves to make.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### tictactoe 
from typing import *
def f_gold(moves: List[List[int]]) -> str:
    n = len(moves)
    counter = [0] * 8
    for i in range(n - 1, -1, -2):
        row, col = moves[i][0], moves[i][1]
        counter[row] += 1
        counter[col + 3] += 1
        if row == col:
            counter[6] += 1
        if row + col == 2:
            counter[7] += 1
        if (
            counter[row] == 3
            or counter[col + 3] == 3
            or counter[6] == 3
            or counter[7] == 3
        ):
            return "A" if (i % 2) == 0 else "B"
    return "Draw" if n == 9 else "Pending"
"-----------------"
test()

