### reverseParentheses 
from typing import *
def f_gold(s: str) -> str:
    stack = []
    for c in s:
        if c == ")":
            tmp = []
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()
            stack += tmp
        else:
            stack.append(c)
    return "".join(stack)