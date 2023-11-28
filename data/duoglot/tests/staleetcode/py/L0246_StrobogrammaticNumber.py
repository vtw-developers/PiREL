
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["69"]
    # output: true
    ,
    # example 2
    ["88"]
    # output: true
    ,
    # example 3
    ["962"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isStrobogrammatic 
from typing import *
def f_gold(num: str) -> bool:
    def match(a, b):
        if a in {'0', '1', '8'}:
            return a == b
        if a == '6':
            return b == '9'
        if a == '9':
            return b == '6'
        return False
    n = len(num)
    i, j = 0, n - 1
    while i <= j:
        if not match(num[i], num[j]):
            return False
        i += 1
        j -= 1
    return True
"-----------------"
test()

