
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 1, 2]]
    # output: true
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: false
    ,
    # example 3
    [[1, 1, 1, 1]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isSelfCrossing 
from typing import *
def f_gold(distance: List[int]) -> bool:
    d = distance
    for i in range(3, len(d)):
        if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
            return True
        if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
            return True
        if (
            i >= 5
            and d[i - 2] >= d[i - 4]
            and d[i - 1] <= d[i - 3]
            and d[i] >= d[i - 2] - d[i - 4]
            and d[i - 1] + d[i - 5] >= d[i - 3]
        ):
            return True
    return False
"-----------------"
test()

