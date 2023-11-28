
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9, 9, 6, 0, 6, 6, 9]]
    # output: 3
    # EXPLANATION: The longest well-performing interval is [9,9,6].
    ,
    # example 2
    [[6, 6, 6]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestWPI 
from typing import *
def f_gold(hours: List[int]) -> int:
    ans = s = 0
    seen = {}
    for i, h in enumerate(hours):
        s += 1 if h > 8 else -1
        if s > 0:
            ans = i + 1
        else:
            if s not in seen:
                seen[s] = i
            if s - 1 in seen:
                ans = max(ans, i - seen[s - 1])
    return ans
"-----------------"
test()

