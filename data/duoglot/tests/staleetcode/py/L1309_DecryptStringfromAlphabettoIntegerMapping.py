
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["10#11#12"]
    # output: "jkab"
    # EXPLANATION:  "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
    ,
    # example 2
    ["1326#"]
    # output: "acz"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### freqAlphabets 
from typing import *
def f_gold(s: str) -> str:
    def get(s):
        return chr(ord('a') + int(s) - 1)
    i, n = 0, len(s)
    res = []
    while i < n:
        if i + 2 < n and s[i + 2] == '#':
            res.append(get(s[i : i + 2]))
            i += 3
        else:
            res.append(get(s[i]))
            i += 1
    return ''.join(res)
"-----------------"
test()

