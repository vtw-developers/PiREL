
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["5F3Z-2e-9-w", 4]
    # output: "5F3Z-2E9W"
    # EXPLANATION:  The string s has been split into two parts, each part has 4 characters. Note that the two extra dashes are not needed and can be removed.
    ,
    # example 2
    ["2-5g-3-J", 2]
    # output: "2-5G-3J"
    # EXPLANATION:  The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### licenseKeyFormatting 
from typing import *
def f_gold(s: str, k: int) -> str:
    s = s.replace('-', '').upper()
    res = []
    cnt = (len(s) % k) or k
    t = 0
    for i, c in enumerate(s):
        res.append(c)
        t += 1
        if t == cnt:
            t = 0
            cnt = k
            if i != len(s) - 1:
                res.append('-')
    return ''.join(res)
"-----------------"
test()

