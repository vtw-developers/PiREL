
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]]
    # output: 3
    # EXPLANATION:  The image shows the costs of connecting houses using pipes. The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
    ,
    # example 2
    [2, [1, 1], [[1, 2, 1], [1, 2, 2]]]
    # output: 2
    # EXPLANATION:  We can supply water with cost two using one of the three options: Option 1:   - Build a well inside house 1 with cost 1.   - Build a well inside house 2 with cost 1. The total cost will be 2. Option 2:   - Build a well inside house 1 with cost 1.   - Connect house 2 with house 1 with cost 1. The total cost will be 2. Option 3:   - Build a well inside house 2 with cost 1.   - Connect house 1 with house 2 with cost 1. The total cost will be 2. Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose <strong>the cheapest option</strong>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minCostToSupplyWater 
from typing import *
def f_gold(n: int, wells: List[int], pipes: List[List[int]]
) -> int:
    for i, w in enumerate(wells):
        pipes.append([0, i + 1, w])
    pipes.sort(key=lambda x: x[2])
    p = list(range(n + 1))
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    res = 0
    for u, v, w in pipes:
        if find(u) == find(v):
            continue
        p[find(u)] = find(v)
        res += w
        n -= 1
        if n == 0:
            break
    return res
"-----------------"
test()

