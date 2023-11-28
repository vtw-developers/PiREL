
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [[1, 2]]]
    # output: 2
    ,
    # example 2
    [3, [[1, 3], [2, 3]]]
    # output: 3
    ,
    # example 3
    [3, [[1, 3], [2, 3], [3, 1]]]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findJudge 
from typing import *
def f_gold(n: int, trust: List[List[int]]) -> int:
    N = 1001
    c1, c2 = [0] * N, [0] * N
    for a, b in trust:
        c1[a] += 1
        c2[b] += 1
    for i in range(1, N):
        if c1[i] == 0 and c2[i] == n - 1:
            return i
    return -1
"-----------------"
test()

