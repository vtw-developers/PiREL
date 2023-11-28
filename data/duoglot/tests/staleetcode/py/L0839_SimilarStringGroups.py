
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["tars", "rats", "arts", "star"]]
    # output: 2
    ,
    # example 2
    [["omv", "ovm"]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSimilarGroups 
from typing import *
def f_gold(strs: List[str]) -> int:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    n, l = len(strs), len(strs[0])
    p = list(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if sum(strs[i][k] != strs[j][k] for k in range(l)) <= 2:
                p[find(i)] = find(j)
    return sum(i == find(i) for i in range(n))
"-----------------"
test()

