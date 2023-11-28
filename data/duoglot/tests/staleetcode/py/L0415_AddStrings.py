
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["11", "123"]
    # output: "134"
    ,
    # example 2
    ["456", "77"]
    # output: "533"
    ,
    # example 3
    ["0", "0"]
    # output: "0"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### addStrings 
from typing import *
def f_gold(num1: str, num2: str) -> str:
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    ans = []
    while i >= 0 or j >= 0 or carry:
        carry += (0 if i < 0 else int(num1[i])) + (0 if j < 0 else int(num2[j]))
        carry, v = divmod(carry, 10)
        ans.append(str(v))
        i, j = i - 1, j - 1
    return ''.join(ans[::-1])
"-----------------"
test()

