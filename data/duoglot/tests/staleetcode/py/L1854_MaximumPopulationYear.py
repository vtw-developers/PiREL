
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1993, 1999], [2000, 2010]]]
    # output: 1993
    # EXPLANATION:  The maximum population is 1, and 1993 is the earliest year with this population.
    ,
    # example 2
    [[[1950, 1961], [1960, 1971], [1970, 1981]]]
    # output: 1960
    # EXPLANATION:   The maximum population is 2, and it had happened in years 1960 and 1970. The earlier year between them is 1960.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumPopulation 
from typing import *
def f_gold(logs: List[List[int]]) -> int:
    delta = [0] * 2055
    for birth, death in logs:
        delta[birth] += 1
        delta[death] -= 1
    mx = res = cur = 0
    for i, v in enumerate(delta):
        cur += v
        if mx < cur:
            mx = cur
            res = i
    return res
"-----------------"
test()

