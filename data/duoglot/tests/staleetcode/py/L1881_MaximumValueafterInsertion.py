
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["99", 9]
    # output: "999"
    # EXPLANATION:  The result is the same regardless of where you insert 9.
    ,
    # example 2
    ["-13", 2]
    # output: "-123"
    # EXPLANATION:  You can make n one of {-213, -123, -132}, and the largest of those three is -123.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxValue 
from typing import *
def f_gold(n: str, x: int) -> str:
    negative = n[0] == '-'
    i, res = 0, []
    if negative:
        i += 1
        res.append('-')
    find = False
    while i < len(n):
        num = int(n[i])
        if (negative and x < num) or (not negative and x > num):
            res.append(str(x))
            find = True
            break
        res.append(n[i])
        i += 1
    res.append(n[i:] if find else str(x))
    return ''.join(res)
"-----------------"
test()

