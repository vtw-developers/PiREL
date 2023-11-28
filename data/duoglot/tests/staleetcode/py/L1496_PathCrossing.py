
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["NES"]
    # output: false
    # EXPLANATION:  Notice that the path doesn't cross any point more than once.
    ,
    # example 2
    ["NESWW"]
    # output: true
    # EXPLANATION:  Notice that the path visits the origin twice.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isPathCrossing 
from typing import *
def f_gold(path: str) -> bool:
    x = y = 0
    vis = {(x, y)}
    for c in path:
        if c == 'N':
            y += 1
        elif c == 'S':
            y -= 1
        elif c == 'E':
            x += 1
        else:
            x -= 1
        if (x, y) in vis:
            return True
        vis.add((x, y))
    return False
"-----------------"
test()

