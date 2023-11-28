
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]]
    # output: 2
    ,
    # example 2
    [[[1], [1], [1]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### leastBricks 
from collections import defaultdict
from typing import *
def f_gold(wall: List[List[int]]) -> int:
    cnt = defaultdict(int)
    for row in wall:
        width = 0
        for brick in row[:-1]:
            width += brick
            cnt[width] += 1
    if not cnt:
        return len(wall)
    return len(wall) - cnt[max(cnt, key=cnt.get)]
"-----------------"
test()

