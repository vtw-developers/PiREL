
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abba", "dog cat cat dog"]
    # output: true
    ,
    # example 2
    ["abba", "dog cat cat fish"]
    # output: false
    ,
    # example 3
    ["aaaa", "dog cat cat dog"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### wordPattern 
from collections import defaultdict
from typing import *
def f_gold(pattern: str, s: str) -> bool:
    s = s.split(' ')
    n = len(pattern)
    if n != len(s):
        return False
    c2str, str2c = defaultdict(), defaultdict()
    for i in range(n):
        k, v = pattern[i], s[i]
        if k in c2str and c2str[k] != v:
            return False
        if v in str2c and str2c[v] != k:
            return False
        c2str[k], str2c[v] = v, k
    return True
"-----------------"
test()

