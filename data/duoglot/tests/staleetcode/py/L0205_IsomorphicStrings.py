
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["egg", "add"]
    # output: true
    ,
    # example 2
    ["foo", "bar"]
    # output: false
    ,
    # example 3
    ["paper", "title"]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isIsomorphic 
from typing import *
def f_gold(s: str, t: str) -> bool:
    d1, d2 = [0] * 256, [0] * 256
    for i, (a, b) in enumerate(zip(s, t)):
        a, b = ord(a), ord(b)
        if d1[a] != d2[b]:
            return False
        d1[a] = d2[b] = i + 1
    return True
"-----------------"
test()

