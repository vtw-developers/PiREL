
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1100101"]
    # output: 5
    # EXPLANATION:   One way to remove all the cars containing illegal goods from the sequence is to - remove a car from the left end 2 times. Time taken is 2 * 1 = 2. - remove a car from the right end. Time taken is 1. - remove the car containing illegal goods found in the middle. Time taken is 2. This obtains a total time of 2 + 1 + 2 = 5.   An alternative way is to - remove a car from the left end 2 times. Time taken is 2 * 1 = 2. - remove a car from the right end 3 times. Time taken is 3 * 1 = 3. This also obtains a total time of 2 + 3 = 5.  5 is the minimum time taken to remove all the cars containing illegal goods.  There are no other ways to remove them with less time.
    ,
    # example 2
    ["0010"]
    # output: 2
    # EXPLANATION:  One way to remove all the cars containing illegal goods from the sequence is to - remove a car from the left end 3 times. Time taken is 3 * 1 = 3. This obtains a total time of 3.  Another way to remove all the cars containing illegal goods from the sequence is to - remove the car containing illegal goods found in the middle. Time taken is 2. This obtains a total time of 2.  Another way to remove all the cars containing illegal goods from the sequence is to  - remove a car from the right end 2 times. Time taken is 2 * 1 = 2.  This obtains a total time of 2.  2 is the minimum time taken to remove all the cars containing illegal goods.  There are no other ways to remove them with less time.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumTime 
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    pre = [0] * (n + 1)
    suf = [0] * (n + 1)
    for i, c in enumerate(s):
        pre[i + 1] = pre[i] if c == '0' else min(pre[i] + 2, i + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] if s[i] == '0' else min(suf[i + 1] + 2, n - i)
    return min(a + b for a, b in zip(pre[1:], suf[1:]))
"-----------------"
test()

