
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: 12
    # EXPLANATION:  For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
    ,
    # example 2
    [100]
    # output: 682289015
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numPrimeArrangements 
import math
from math import factorial
from typing import *
def f_gold(n: int) -> int:
    def count(n):
        cnt = 0
        primes = [True] * (n + 1)
        for i in range(2, n + 1):
            if primes[i]:
                cnt += 1
                for j in range(i + i, n + 1, i):
                    primes[j] = False
        return cnt
    cnt = count(n)
    ans = factorial(cnt) * factorial(n - cnt)
    return ans % (10**9 + 7)
"-----------------"
test()

