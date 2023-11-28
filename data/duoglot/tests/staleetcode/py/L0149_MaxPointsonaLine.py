
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [2, 2], [3, 3]]]
    # output: 3
    ,
    # example 2
    [[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxPoints 
import math
from math import gcd
from collections import Counter
from typing import *
def f_gold(points: List[List[int]]) -> int:
    def gcd(a, b) -> int:
        return a if b == 0 else gcd(b, a % b)
    n = len(points)
    if n < 3:
        return n
    res = 0
    for i in range(n - 1):
        counter = Counter()
        t_max = duplicate = 0
        for j in range(i + 1, n):
            delta_x = points[i][0] - points[j][0]
            delta_y = points[i][1] - points[j][1]
            if delta_x == 0 and delta_y == 0:
                duplicate += 1
                continue
            g = gcd(delta_x, delta_y)
            d_x = delta_x // g
            d_y = delta_y // g
            key = f'{d_x}.{d_y}'
            counter[key] += 1
            t_max = max(t_max, counter[key])
        res = max(res, t_max + duplicate + 1)
    return res
"-----------------"
test()

