
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10, 3]
    # output: 3
    # EXPLANATION:  10/3 = 3.33333.. which is truncated to 3.
    ,
    # example 2
    [7, -3]
    # output: -2
    # EXPLANATION:  7/-3 = -2.33333.. which is truncated to -2.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### divide 
from typing import *
def f_gold(a: int, b: int) -> int:
    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)
    sign = -1 if a * b < 0 else 1
    a = abs(a)
    b = abs(b)
    tot = 0
    while a >= b:
        cnt = 0
        while a >= (b << (cnt + 1)):
            cnt += 1
        tot += 1 << cnt
        a -= b << cnt
    return sign * tot if INT_MIN <= sign * tot <= INT_MAX else INT_MAX
"-----------------"
test()

