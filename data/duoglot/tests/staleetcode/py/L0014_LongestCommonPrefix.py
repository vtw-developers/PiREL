
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["flower", "flow", "flight"]]
    # output: "fl"
    ,
    # example 2
    [["dog", "racecar", "car"]]
    # output: ""
    # EXPLANATION:  There is no common prefix among the input strings.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestCommonPrefix 
from typing import *
def f_gold(strs: List[str]) -> str:
    n = len(strs)
    if n == 0:
        return ''
    for i in range(len(strs[0])):
        for j in range(1, n):
            if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]
"-----------------"
test()

