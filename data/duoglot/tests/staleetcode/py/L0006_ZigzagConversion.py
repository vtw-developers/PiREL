
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["PAYPALISHIRING", 3]
    # output: "PAHNAPLSIIGYIR"
    ,
    # example 2
    ["PAYPALISHIRING", 4]
    # output: "PINALSIGYAHRPI"
    # EXPLANATION:  P     I    N A   L S  I G Y A   H R P     I
    ,
    # example 3
    ["A", 1]
    # output: "A"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### convert 
from typing import *
def f_gold(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    group = 2 * numRows - 2
    ans = []
    for i in range(1, numRows + 1):
        interval = group if i == numRows else 2 * numRows - 2 * i
        idx = i - 1
        while idx < len(s):
            ans.append(s[idx])
            idx += interval
            interval = group - interval
            if interval == 0:
                interval = group
    return ''.join(ans)
"-----------------"
test()

