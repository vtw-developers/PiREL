
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[17, 2, 17], [16, 16, 5], [14, 3, 19]]]
    # output: 10
    # EXPLANATION:  Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
    ,
    # example 2
    [[[7, 6, 2]]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCost 
from typing import *
def f_gold(costs: List[List[int]]) -> int:
    r, g, b = 0, 0, 0
    for cost in costs:
        _r, _g, _b = r, g, b
        r = min(_g, _b) + cost[0]
        g = min(_r, _b) + cost[1]
        b = min(_r, _g) + cost[2]
    return min(r, g, b)
"-----------------"
test()

