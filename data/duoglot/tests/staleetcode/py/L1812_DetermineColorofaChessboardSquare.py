
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a1"]
    # output: false
    # EXPLANATION:  From the chessboard above, the square with coordinates "a1" is black, so return false.
    ,
    # example 2
    ["h3"]
    # output: true
    # EXPLANATION:  From the chessboard above, the square with coordinates "h3" is white, so return true.
    ,
    # example 3
    ["c7"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### squareIsWhite 
from typing import *
def f_gold(coordinates: str) -> bool:
    x = ord(coordinates[0]) - ord('a') + 1
    y = int(coordinates[1])
    return ((x + y) & 1) == 1
"-----------------"
test()

