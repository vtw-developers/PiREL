
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 2
    # EXPLANATION:  The only integers less than or equal to 4 whose digit sums are even are 2 and 4.
    ,
    # example 2
    [30]
    # output: 14
    # EXPLANATION:  The 14 integers less than or equal to 30 whose digit sums are even are 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countEven 
from typing import *
def f_gold(num: int) -> int:
    ans = 0
    for i in range(1, num + 1):
        t = 0
        while i:
            t += i % 10
            i //= 10
        if t % 2 == 0:
            ans += 1
    return ans
"-----------------"
test()

