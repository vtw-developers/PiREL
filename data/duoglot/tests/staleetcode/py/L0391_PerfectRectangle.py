
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]]
    # output: true
    # EXPLANATION:  All 5 rectangles together form an exact cover of a rectangular region.
    ,
    # example 2
    [[[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]]
    # output: false
    # EXPLANATION:  Because there is a gap between the two rectangular regions.
    ,
    # example 3
    [[[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]]
    # output: false
    # EXPLANATION:  Because two of the rectangles overlap with each other.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isRectangleCover 
from collections import defaultdict
from typing import *
def f_gold(rectangles: List[List[int]]) -> bool:
    area = 0
    minX, minY = rectangles[0][0], rectangles[0][1]
    maxX, maxY = rectangles[0][2], rectangles[0][3]
    cnt = defaultdict(int)
    for r in rectangles:
        area += (r[2] - r[0]) * (r[3] - r[1])
        minX = min(minX, r[0])
        minY = min(minY, r[1])
        maxX = max(maxX, r[2])
        maxY = max(maxY, r[3])
        cnt[(r[0], r[1])] += 1
        cnt[(r[0], r[3])] += 1
        cnt[(r[2], r[3])] += 1
        cnt[(r[2], r[1])] += 1
    if (
        area != (maxX - minX) * (maxY - minY)
        or cnt[(minX, minY)] != 1
        or cnt[(minX, maxY)] != 1
        or cnt[(maxX, maxY)] != 1
        or cnt[(maxX, minY)] != 1
    ):
        return False
    del cnt[(minX, minY)], cnt[(minX, maxY)], cnt[(maxX, maxY)], cnt[(maxX, minY)]
    return all(c == 2 or c == 4 for c in cnt.values())
"-----------------"
test()

