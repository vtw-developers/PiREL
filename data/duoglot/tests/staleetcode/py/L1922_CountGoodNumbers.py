
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 5
    # EXPLANATION:  The good numbers of length 1 are "0", "2", "4", "6", "8".
    ,
    # example 2
    [4]
    # output: 400
    ,
    # example 3
    [50]
    # output: 564908303
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countGoodNumbers 
from typing import *
def f_gold(n: int) -> int:
    mod = 10**9 + 7
    def myPow(x, n):
        res = 1
        while n:
            if (n & 1) == 1:
                res = res * x % mod
            x = x * x % mod
            n >>= 1
        return res
    return myPow(5, (n + 1) >> 1) * myPow(4, n >> 1) % mod
"-----------------"
test()

