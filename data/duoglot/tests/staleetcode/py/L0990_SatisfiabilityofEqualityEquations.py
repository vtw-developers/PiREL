
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a==b", "b!=a"]]
    # output: false
    # EXPLANATION:  If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second. There is no way to assign the variables to satisfy both equations.
    ,
    # example 2
    [["b==a", "a==b"]]
    # output: true
    # EXPLANATION:  We could assign a = 1 and b = 1 to satisfy both equations.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### equationsPossible 
from typing import *
def f_gold(equations: List[str]) -> bool:
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    p = list(range(26))
    for e in equations:
        a, b = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
        if e[1] == '=':
            p[find(a)] = find(b)
    for e in equations:
        a, b = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
        if e[1] == '!' and find(a) == find(b):
            return False
    return True
"-----------------"
test()

