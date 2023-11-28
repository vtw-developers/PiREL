
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: 2
    # EXPLANATION:  5 = 2 + 3
    ,
    # example 2
    [9]
    # output: 3
    # EXPLANATION:  9 = 4 + 5 = 2 + 3 + 4
    ,
    # example 3
    [15]
    # output: 4
    # EXPLANATION:  15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### consecutiveNumbersSum 
from typing import *
def f_gold(n: int) -> int:
    n <<= 1
    ans, k = 0, 1
    while k * (k + 1) <= n:
        if n % k == 0 and (n // k + 1 - k) % 2 == 0:
            ans += 1
        k += 1
    return ans
"-----------------"
test()

