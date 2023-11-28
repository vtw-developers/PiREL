
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 1], [1, 1]]]
    # output: 1
    # EXPLANATION:  After flipping no values, 1 row has all values equal.
    ,
    # example 2
    [[[0, 1], [1, 0]]]
    # output: 2
    # EXPLANATION:  After flipping values in the first column, both rows have equal values.
    ,
    # example 3
    [[[0, 0, 0], [0, 0, 1], [1, 1, 0]]]
    # output: 2
    # EXPLANATION:  After flipping values in the first two columns, the last two rows have equal values.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxEqualRowsAfterFlips 
from collections import Counter
from typing import *
def f_gold(matrix: List[List[int]]) -> int:
    cnt = Counter()
    for row in matrix:
        t = []
        for v in row:
            if row[0] == 1:
                v ^= 1
            t.append(str(v))
        s = ''.join(t)
        cnt[s] += 1
    return max(cnt.values())
"-----------------"
test()

