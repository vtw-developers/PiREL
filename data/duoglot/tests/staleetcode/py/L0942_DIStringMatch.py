
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["IDID"]
    # output: [0,4,1,3,2]
    ,
    # example 2
    ["III"]
    # output: [0,1,2,3]
    ,
    # example 3
    ["DDI"]
    # output: [3,2,0,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### diStringMatch 
from typing import *
def f_gold(s: str) -> List[int]:
    n = len(s)
    low, high = 0, n
    ans = []
    for i in range(n):
        if s[i] == 'I':
            ans.append(low)
            low += 1
        else:
            ans.append(high)
            high -= 1
    ans.append(low)
    return ans
"-----------------"
test()

