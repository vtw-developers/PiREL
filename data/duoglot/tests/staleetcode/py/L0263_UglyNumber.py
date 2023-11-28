
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6]
    # output: true
    # EXPLANATION:  6 = 2   3
    ,
    # example 2
    [1]
    # output: true
    # EXPLANATION:  1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
    ,
    # example 3
    [14]
    # output: false
    # EXPLANATION:  14 is not ugly since it includes the prime factor 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isUgly 
from typing import *
def f_gold(n: int) -> bool:
    if n < 1:
        return False
    for x in [2, 3, 5]:
        while n % x == 0:
            n //= x
    return n == 1
"-----------------"
test()

