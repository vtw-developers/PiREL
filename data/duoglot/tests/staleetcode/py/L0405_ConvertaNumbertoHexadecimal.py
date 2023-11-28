
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [26]
    # output: "1a"
    ,
    # example 2
    [-1]
    # output: "ffffffff"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### toHex 
from typing import *
def f_gold(num: int) -> str:
    if num == 0:
        return '0'
    chars = '0123456789abcdef'
    s = []
    for i in range(7, -1, -1):
        x = (num >> (4 * i)) & 0xF
        if s or x != 0:
            s.append(chars[x])
    return ''.join(s)
"-----------------"
test()

