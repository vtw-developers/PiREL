
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["3+2*2"]
    # output: 7
    ,
    # example 2
    [" 3/2 "]
    # output: 1
    ,
    # example 3
    [" 3+5 / 2 "]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### calculate 
from typing import *
def f_gold(s: str) -> int:
    num, n = 0, len(s)
    pre_sign = '+'
    stack = []
    for i in range(n):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if i == n - 1 or (not s[i].isdigit() and s[i] != ' '):
            if pre_sign == '+':
                stack.append(num)
            elif pre_sign == '-':
                stack.append(-num)
            elif pre_sign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            pre_sign = s[i]
            num = 0
    res = 0
    while stack:
        res += stack.pop()
    return res
"-----------------"
test()

