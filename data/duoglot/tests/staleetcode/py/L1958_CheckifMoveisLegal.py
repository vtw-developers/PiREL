
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], 4, 3, "B"]
    # output: true
    # EXPLANATION:  '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'. The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
    ,
    # example 2
    [[[".", ".", ".", ".", ".", ".", ".", "."], [".", "B", ".", ".", "W", ".", ".", "."], [".", ".", "W", ".", ".", ".", ".", "."], [".", ".", ".", "W", "B", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "B", "W", ".", "."], [".", ".", ".", ".", ".", ".", "W", "."], [".", ".", ".", ".", ".", ".", ".", "B"]], 4, 4, "W"]
    # output: false
    # EXPLANATION:  While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkMove 
from typing import *
def f_gold(board: List[List[str]], rMove: int, cMove: int, color: str
) -> bool:
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    n = 8
    for a, b in dirs:
        i, j = rMove, cMove
        t = 0
        while 0 <= i + a < n and 0 <= j + b < n:
            t += 1
            i, j = i + a, j + b
            if board[i][j] in ['.', color]:
                break
        if board[i][j] == color and t > 1:
            return True
    return False
"-----------------"
test()

