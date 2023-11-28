
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["UD"]
    # output: true
    # EXPLANATION: : The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
    ,
    # example 2
    ["LL"]
    # output: false
    # EXPLANATION: : The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### judgeCircle 
from typing import *
def f_gold(moves: str) -> bool:
    x = y = 0
    for c in moves:
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
    return x == 0 and y == 0
"-----------------"
test()

