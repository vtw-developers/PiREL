
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3]
    # output: 16
    # EXPLANATION:  The bookstore owner keeps themselves not grumpy for the last 3 minutes.  The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
    ,
    # example 2
    [[1], [0], 1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxSatisfied 
from typing import *
def f_gold(customers: List[int], grumpy: List[int], minutes: int
) -> int:
    s = sum(a * b for a, b in zip(customers, grumpy))
    cs = sum(customers)
    t = ans = 0
    for i, (a, b) in enumerate(zip(customers, grumpy), 1):
        t += a * b
        if (j := i - minutes) >= 0:
            ans = max(ans, cs - (s - t))
            t -= customers[j] * grumpy[j]
    return ans
"-----------------"
test()

