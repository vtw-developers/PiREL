
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["00110"]
    # output: 1
    # EXPLANATION:  We flip the last digit to get 00111.
    ,
    # example 2
    ["010110"]
    # output: 2
    # EXPLANATION:  We flip to get 011111, or alternatively 000111.
    ,
    # example 3
    ["00011000"]
    # output: 2
    # EXPLANATION:  We flip to get 00000000.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minFlipsMonoIncr 
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    left, right = [0] * (n + 1), [0] * (n + 1)
    ans = 0x3F3F3F3F
    for i in range(1, n + 1):
        left[i] = left[i - 1] + (1 if s[i - 1] == '1' else 0)
    for i in range(n - 1, -1, -1):
        right[i] = right[i + 1] + (1 if s[i] == '0' else 0)
    for i in range(0, n + 1):
        ans = min(ans, left[i] + right[i])
    return ans
"-----------------"
test()

