
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [8]
    # output: 3
    # EXPLANATION:  8 -> 4 -> 2 -> 1
    ,
    # example 2
    [7]
    # output: 4
    # EXPLANATION: 7 -> 8 -> 4 -> 2 -> 1 or 7 -> 6 -> 3 -> 2 -> 1
    ,
    # example 3
    [4]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### integerReplacement 
from typing import *
def f_gold(n: int) -> int:
    ans = 0
    while n != 1:
        if (n & 1) == 0:
            n >>= 1
        elif n != 3 and (n & 3) == 3:
            n += 1
        else:
            n -= 1
        ans += 1
    return ans
"-----------------"
test()

