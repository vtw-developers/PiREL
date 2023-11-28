
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["bab", "aba"]
    # output: 1
    # EXPLANATION:  Replace the first 'a' in t with b, t = "bba" which is anagram of s.
    ,
    # example 2
    ["leetcode", "practice"]
    # output: 5
    # EXPLANATION:  Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
    ,
    # example 3
    ["anagram", "mangaar"]
    # output: 0
    # EXPLANATION:  "anagram" and "mangaar" are anagrams.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSteps 
from collections import Counter
from typing import *
def f_gold(s: str, t: str) -> int:
    counter = Counter(s)
    res = 0
    for c in t:
        if counter[c] > 0:
            counter[c] -= 1
        else:
            res += 1
    return res
"-----------------"
test()

