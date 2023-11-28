
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]]
    # output: 3
    # EXPLANATION:  All the three 'B's are black lonely pixels.
    ,
    # example 2
    [[["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findLonelyPixel 
from typing import *
def f_gold(picture: List[List[str]]) -> int:
    m, n = len(picture), len(picture[0])
    rows, cols = [0] * m, [0] * n
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 'B':
                rows[i] += 1
                cols[j] += 1
    res = 0
    for i in range(m):
        if rows[i] == 1:
            for j in range(n):
                if picture[i][j] == 'B' and cols[j] == 1:
                    res += 1
                    break
    return res
"-----------------"
test()

