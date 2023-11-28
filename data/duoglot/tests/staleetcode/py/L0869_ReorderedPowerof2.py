
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: true
    ,
    # example 2
    [10]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reorderedPowerOf2 
from typing import *
def f_gold(n: int) -> bool:
    def convert(n):
        counter = [0] * 10
        while n > 0:
            counter[n % 10] += 1
            n //= 10
        return counter
    i, s = 1, convert(n)
    while i <= 10**9:
        if convert(i) == s:
            return True
        i <<= 1
    return False
"-----------------"
test()

