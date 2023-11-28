
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [10]
    # output: 4
    # EXPLANATION:  There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    ,
    # example 2
    [0]
    # output: 0
    ,
    # example 3
    [1]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countPrimes 
from typing import *
def f_gold(n: int) -> int:
    primes = [True] * n
    ans = 0
    for i in range(2, n):
        if primes[i]:
            ans += 1
            for j in range(i + i, n, i):
                primes[j] = False
    return ans
"-----------------"
test()

