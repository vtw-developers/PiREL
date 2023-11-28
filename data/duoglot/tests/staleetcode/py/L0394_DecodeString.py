
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["3[a]2[bc]"]
    # output: "aaabcbc"
    ,
    # example 2
    ["3[a2[c]]"]
    # output: "accaccacc"
    ,
    # example 3
    ["2[abc]3[cd]ef"]
    # output: "abcabccdcdcdef"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### decodeString 
from typing import *
def f_gold(s: str) -> str:
    s1, s2 = [], []
    num, res = 0, ''
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            s1.append(num)
            s2.append(res)
            num, res = 0, ''
        elif c == ']':
            res = s2.pop() + res * s1.pop()
        else:
            res += c
    return res
"-----------------"
test()

