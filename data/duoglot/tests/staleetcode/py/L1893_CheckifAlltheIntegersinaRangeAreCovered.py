
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3, 4], [5, 6]], 2, 5]
    # output: true
    # EXPLANATION:  Every integer between 2 and 5 is covered: - 2 is covered by the first range. - 3 and 4 are covered by the second range. - 5 is covered by the third range.
    ,
    # example 2
    [[[1, 10], [10, 20]], 21, 21]
    # output: false
    # EXPLANATION:  21 is not covered by any range.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isCovered 
from typing import *
def f_gold(ranges: List[List[int]], left: int, right: int) -> bool:
    diff = [0] * 52
    for l, r in ranges:
        diff[l] += 1
        diff[r + 1] -= 1
    cur = 0
    for i, df in enumerate(diff):
        cur += df
        if left <= i <= right and cur == 0:
            return False
    return True
"-----------------"
test()

