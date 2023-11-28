
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]]
    # output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    # EXPLANATION:   Given: <em>a / b = 2.0</em>, <em>b / c = 3.0</em> queries are: <em>a / c = ?</em>, <em>b / a = ?</em>, <em>a / e = ?</em>, <em>a / a = ?</em>, <em>x / x = ?</em> return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    ,
    # example 2
    [[["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]]
    # output: [3.75000,0.40000,5.00000,0.20000]
    ,
    # example 3
    [[["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]]
    # output: [0.50000,2.00000,-1.00000,-1.00000]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### calcEquation 
from collections import defaultdict
from typing import *
def f_gold(equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    def find(x):
        if p[x] != x:
            origin = p[x]
            p[x] = find(p[x])
            w[x] *= w[origin]
        return p[x]
    w = defaultdict(lambda: 1)
    p = defaultdict()
    for a, b in equations:
        p[a], p[b] = a, b
    for i, v in enumerate(values):
        a, b = equations[i]
        pa, pb = find(a), find(b)
        if pa == pb:
            continue
        p[pa] = pb
        w[pa] = w[b] * v / w[a]
    return [
        -1 if c not in p or d not in p or find(c) != find(d) else w[c] / w[d]
        for c, d in queries
    ]
"-----------------"
test()

