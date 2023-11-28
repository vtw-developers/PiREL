
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3]
    # output: 2
    # EXPLANATION:  arr = [1, 3, 5] First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4] In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
    ,
    # example 2
    [6]
    # output: 9
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minOperations 
from typing import *
def f_gold(n: int) -> int:
    ans = 0
    for i in range(n >> 1):
        ans += n - (2 * i + 1)
    return ans
"-----------------"
test()

