
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["annabelle", 2]
    # output: true
    # EXPLANATION:  You can construct two palindromes using all characters in s. Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
    ,
    # example 2
    ["leetcode", 3]
    # output: false
    # EXPLANATION:  It is impossible to construct 3 palindromes using all the characters of s.
    ,
    # example 3
    ["True", 4]
    # output: true
    # EXPLANATION:  The only possible solution is to put each character in a separate string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canConstruct 
from collections import Counter
from typing import *
def f_gold(s: str, k: int) -> bool:
    if len(s) < k:
        return False
    counter = Counter(s)
    cnt = sum(1 for n in counter.values() if n % 2 == 1)
    return cnt <= k
"-----------------"
test()

