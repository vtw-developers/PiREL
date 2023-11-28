
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 1], [3, 4], [5, 6]]]
    # output: 1
    ,
    # example 2
    [[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numEquivDominoPairs 
from collections import Counter
from typing import *
def f_gold(dominoes: List[List[int]]) -> int:
    counter = Counter()
    ans = 0
    for a, b in dominoes:
        v = a * 10 + b if a > b else b * 10 + a
        ans += counter[v]
        counter[v] += 1
    return ans
"-----------------"
test()

