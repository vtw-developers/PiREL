
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]]
    # output: [3,0,3]
    # EXPLANATION:  The nearest 3 from index 1 is at index 4 (3 steps away). The nearest 2 from index 2 is at index 2 itself (0 steps away). The nearest 1 from index 6 is at index 3 (3 steps away).
    ,
    # example 2
    [[1, 2], [[0, 3]]]
    # output: [-1]
    # EXPLANATION: There is no 3 in the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### shortestDistanceColor 
from collections import defaultdict
from typing import *
def f_gold(colors: List[int], queries: List[List[int]]
) -> List[int]:
    color_indexes = defaultdict(list)
    for i, c in enumerate(colors):
        color_indexes[c].append(i)
    res = []
    for i, c in queries:
        if c not in color_indexes:
            res.append(-1)
        else:
            t = color_indexes[c]
            left, right = 0, len(t) - 1
            while left < right:
                mid = (left + right) >> 1
                if t[mid] >= i:
                    right = mid
                else:
                    left = mid + 1
            val = abs(t[left] - i)
            if left > 0:
                val = min(val, abs(t[left - 1] - i))
            if left < len(t) - 1:
                val = min(val, abs(t[left + 1] - i))
            res.append(val)
    return res
"-----------------"
test()

