
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 22
    # EXPLANATION:   22 is numerically balanced since: - The digit 2 occurs 2 times.  It is also the smallest numerically balanced number strictly greater than 1.
    ,
    # example 2
    [1000]
    # output: 1333
    # EXPLANATION:   1333 is numerically balanced since: - The digit 1 occurs 1 time. - The digit 3 occurs 3 times.  It is also the smallest numerically balanced number strictly greater than 1000. Note that 1022 cannot be the answer because 0 appeared more than 0 times.
    ,
    # example 3
    [3000]
    # output: 3133
    # EXPLANATION:   3133 is numerically balanced since: - The digit 1 occurs 1 time. - The digit 3 occurs 3 times. It is also the smallest numerically balanced number strictly greater than 3000.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### nextBeautifulNumber 
from typing import *
def f_gold(n: int) -> int:
    def check(num):
        counter = [0] * 10
        for c in str(num):
            counter[int(c)] += 1
        for c in str(num):
            if counter[int(c)] != int(c):
                return False
        return True
    for i in range(n + 1, 10**7):
        if check(i):
            return i
    return -1
"-----------------"
test()

