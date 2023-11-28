
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 10
    # EXPLANATION:  After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
    ,
    # example 2
    [10]
    # output: 37
    # EXPLANATION:  After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
    ,
    # example 3
    [20]
    # output: 96
    # EXPLANATION:  After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### totalMoney 
from typing import *
def f_gold(n: int) -> int:
    a, b = divmod(n, 7)
    return (28 + 28 + 7 * (a - 1)) * a // 2 + (a * 2 + b + 1) * b // 2
"-----------------"
test()

