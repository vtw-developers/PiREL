
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [28]
    # output: true
    # EXPLANATION:  28 = 1 + 2 + 4 + 7 + 14 1, 2, 4, 7, and 14 are all divisors of 28.
    ,
    # example 2
    [7]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkPerfectNumber 
from typing import *
def f_gold(num: int) -> bool:
    if num == 1:
        return False
    s, i = 1, 2
    while i * i <= num:
        if num % i == 0:
            s += i
            if i != num // i:
                s += num // i
        i += 1
    return s == num
"-----------------"
test()

