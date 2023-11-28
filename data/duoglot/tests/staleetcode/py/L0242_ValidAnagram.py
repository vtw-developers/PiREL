
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["anagram", "nagaram"]
    # output: true
    ,
    # example 2
    ["rat", "car"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isAnagram 
from typing import *
def f_gold(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    chars = [0] * 26
    for i in range(len(s)):
        chars[ord(s[i]) - ord('a')] += 1
        chars[ord(t[i]) - ord('a')] -= 1
    return all(c == 0 for c in chars)
"-----------------"
test()

