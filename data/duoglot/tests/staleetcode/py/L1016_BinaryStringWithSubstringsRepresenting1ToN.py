
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["0110", 3]
    # output: true
    ,
    # example 2
    ["0110", 4]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### queryString 
from typing import *
def f_gold(s: str, n: int) -> bool:
    for i in range(n, n // 2, -1):
        if bin(i)[2:] not in s:
            return False
    return True
"-----------------"
test()

