
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["cdbcbbaaabab", 4, 5]
    # output: 19
    # EXPLANATION:  - Remove the "ba" underlined in "cdbcbbaaa<u>ba</u>b". Now, s = "cdbcbbaaab" and 5 points are added to the score. - Remove the "ab" underlined in "cdbcbbaa<u>ab</u>". Now, s = "cdbcbbaa" and 4 points are added to the score. - Remove the "ba" underlined in "cdbcb<u>ba</u>a". Now, s = "cdbcba" and 5 points are added to the score. - Remove the "ba" underlined in "cdbc<u>ba</u>". Now, s = "cdbc" and 5 points are added to the score. Total score = 5 + 4 + 5 + 5 = 19.
    ,
    # example 2
    ["aabbaaxybbaabb", 5, 4]
    # output: 20
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumGain 
from typing import *
def f_gold(s: str, x: int, y: int) -> int:
    if x < y:
        return f_gold(s[::-1], y, x)
    ans = 0
    stk1, stk2 = [], []
    for c in s:
        if c != 'b':
            stk1.append(c)
        else:
            if stk1 and stk1[-1] == 'a':
                stk1.pop()
                ans += x
            else:
                stk1.append(c)
    while stk1:
        c = stk1.pop()
        if c != 'b':
            stk2.append(c)
        else:
            if stk2 and stk2[-1] == 'a':
                stk2.pop()
                ans += y
            else:
                stk2.append(c)
    return ans
"-----------------"
test()

