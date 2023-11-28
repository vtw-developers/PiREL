
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["(()"]
    # output: 2
    # EXPLANATION:  The longest valid parentheses substring is "()".
    ,
    # example 2
    [")()())"]
    # output: 4
    # EXPLANATION:  The longest valid parentheses substring is "()()".
    ,
    # example 3
    [""]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestValidParentheses 
from typing import *
def f_gold(s):
    """
    :type s: string
    :rtype int
    """
    Longest = temp = 0
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) != 0 and stack[-1] == '(':
            stack.pop()
            temp += 2
        else:
            stack = []
            if temp > Longest:
                Longest = temp
            temp = 0
    if temp > Longest:
        Longest = temp
    return Longest
"-----------------"
test()

