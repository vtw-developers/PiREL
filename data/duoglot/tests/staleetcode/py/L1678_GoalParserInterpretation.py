
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["G()(al)"]
    # output: "Goal"
    # EXPLANATION:  The Goal Parser interprets the command as follows: G -> G () -> o (al) -> al The final concatenated result is "Goal".
    ,
    # example 2
    ["G()()()()(al)"]
    # output: "Gooooal"
    ,
    # example 3
    ["(al)G(al)()()G"]
    # output: "alGalooG"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### interpret 
from typing import *
def f_gold(command: str) -> str:
    res = ''
    i, n = 0, len(command)
    while i < n:
        c = command[i]
        if c == 'G':
            res += c
            i += 1
        elif c == '(' and command[i + 1] != ')':
            res += 'al'
            i += 4
        else:
            res += 'o'
            i += 2
    return res
"-----------------"
test()

