
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(()())(())"]
    # output: "()()()"
    # EXPLANATION:   The input string is "(()())(())", with primitive decomposition "(()())" + "(())". After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
    ,
    # example 2
    ["(()())(())(()(()))"]
    # output: "()()()()(())"
    # EXPLANATION:   The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))". After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
    ,
    # example 3
    ["()()"]
    # output: ""
    # EXPLANATION:   The input string is "()()", with primitive decomposition "()" + "()". After removing outer parentheses of each part, this is "" + "" = "".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removeOuterParentheses 
from typing import *
def f_gold(s: str) -> str:
    ans = []
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
            if cnt > 1:
                ans.append(c)
        else:
            cnt -= 1
            if cnt > 0:
                ans.append(c)
    return ''.join(ans)
"-----------------"
test()

