
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcd", "bcdf", 3]
    # output: 3
    # EXPLANATION:  "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
    ,
    # example 2
    ["abcd", "cdef", 3]
    # output: 1
    # EXPLANATION:  Each character in s costs 2 to change to character in t,  so the maximum length is 1.
    ,
    # example 3
    ["abcd", "acde", 0]
    # output: 1
    # EXPLANATION:  You cannot make any change, so the maximum length is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### equalSubstring 
from typing import *
def f_gold(s: str, t: str, maxCost: int) -> int:
    n = len(s)
    presum = [0] * (n + 1)
    for i in range(n):
        presum[i + 1] = presum[i] + abs(ord(s[i]) - ord(t[i]))
    left, right = 0, n
    def check(l):
        i = 0
        while i + l - 1 < n:
            j = i + l - 1
            if presum[j + 1] - presum[i] <= maxCost:
                return True
            i += 1
        return False
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

