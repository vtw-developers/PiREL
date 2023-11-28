
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [3]]
    # output: 8
    ,
    # example 2
    [2, [1, 0]]
    # output: 1024
    ,
    # example 3
    [1, [4, 3, 3, 8, 5, 2]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### superPow 
from typing import *
def f_gold(a: int, b: List[int]) -> int:
    MOD = 1337
    ans = 1
    for e in b[::-1]:
        ans = ans * pow(a, e, MOD) % MOD
        a = pow(a, 10, MOD)
    return ans
"-----------------"
test()

