
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: 3
    ,
    # example 2
    [11]
    # output: 0
    # EXPLANATION:  The 11<sup>th</sup> digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findNthDigit 
from typing import *
def f_gold(n: int) -> int:
    bits, t = 1, 9
    while n > bits * t:
        n -= bits * t
        bits += 1
        t *= 10
    start = 10 ** (bits - 1) + (n // bits) - 1
    if n % bits == 0:
        return start % 10
    return int(str((start + 1))[(n % bits) - 1])
"-----------------"
test()

