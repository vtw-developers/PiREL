
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abccccdd"]
    # output: 7
    # EXPLANATION:  One longest palindrome that can be built is "dccaccd", whose length is 7.
    ,
    # example 2
    ["a"]
    # output: 1
    # EXPLANATION:  The longest palindrome that can be built is "a", whose length is 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestPalindrome 
from collections import Counter
from typing import *
def f_gold(s: str) -> int:
    n = len(s)
    counter = Counter(s)
    odd_cnt = sum(e % 2 for e in counter.values())
    return n if odd_cnt == 0 else n - odd_cnt + 1
"-----------------"
test()

