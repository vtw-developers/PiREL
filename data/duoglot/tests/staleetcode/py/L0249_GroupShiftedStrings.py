
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]]
    # output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    ,
    # example 2
    [["a"]]
    # output: [["a"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### groupStrings 
from collections import defaultdict
from typing import *
def f_gold(strings: List[str]) -> List[List[str]]:
    mp = defaultdict(list)
    for s in strings:
        t = []
        diff = ord(s[0]) - ord('a')
        for c in s:
            d = ord(c) - diff
            if d < ord('a'):
                d += 26
            t.append(chr(d))
        k = ''.join(t)
        mp[k].append(s)
    return list(mp.values())
"-----------------"
test()

