
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["/home/"]
    # output: "/home"
    # EXPLANATION:  Note that there is no trailing slash after the last directory name.
    ,
    # example 2
    ["/../"]
    # output: "/"
    # EXPLANATION:  Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
    ,
    # example 3
    ["/home//foo/"]
    # output: "/home/foo"
    # EXPLANATION:  In the canonical path, multiple consecutive slashes are replaced by a single one.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### simplifyPath 
from typing import *
def f_gold(path: str) -> str:
    stk = []
    for s in path.split('/'):
        if not s or s == '.':
            continue
        if s == '..':
            if stk:
                stk.pop()
        else:
            stk.append(s)
    return '/' + '/'.join(stk)
"-----------------"
test()

