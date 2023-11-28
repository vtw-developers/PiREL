
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["?zs"]
    # output: "azs"
    # EXPLANATION:  There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
    ,
    # example 2
    ["ubv?w"]
    # output: "ubvaw"
    # EXPLANATION:  There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### modifyString 
from typing import *
def f_gold(s: str) -> str:
    ans = list(s)
    for i, c in enumerate(ans):
        if c == '?':
            for cc in 'abc':
                if i > 0 and ans[i - 1] == cc:
                    continue
                if i < len(s) - 1 and ans[i + 1] == cc:
                    continue
                ans[i] = cc
                break
    return ''.join(ans)
"-----------------"
test()

