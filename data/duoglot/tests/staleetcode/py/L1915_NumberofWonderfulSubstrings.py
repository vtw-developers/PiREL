
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aba"]
    # output: 4
    # EXPLANATION:  The four wonderful substrings are underlined below:  - "<u><strong>a</strong></u>ba" -> "a"  - "a<u><strong>b</strong></u>a" -> "b"  - "ab<u><strong>a</strong></u>" -> "a"  - "<u><strong>aba</strong></u>" -> "aba"
    ,
    # example 2
    ["aabb"]
    # output: 9
    # EXPLANATION:  The nine wonderful substrings are underlined below:  - "<strong><u>a</u></strong>abb" -> "a"  - "<u><strong>aa</strong></u>bb" -> "aa"  - "<u><strong>aab</strong></u>b" -> "aab"  - "<u><strong>aabb</strong></u>" -> "aabb"  - "a<u><strong>a</strong></u>bb" -> "a"  - "a<u><strong>abb</strong></u>" -> "abb"  - "aa<u><strong>b</strong></u>b" -> "b"  - "aa<u><strong>bb</strong></u>" -> "bb"  - "aab<u><strong>b</strong></u>" -> "b"
    ,
    # example 3
    ["he"]
    # output: 2
    # EXPLANATION:  The two wonderful substrings are underlined below:  - "<b><u>h</u></b>e" -> "h"  - "h<strong><u>e</u></strong>" -> "e"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### wonderfulSubstrings 
from collections import Counter
from typing import *
def f_gold(word: str) -> int:
    counter = Counter({0: 1})
    state = 0
    ans = 0
    for c in word:
        state ^= 1 << (ord(c) - ord('a'))
        ans += counter[state]
        for i in range(10):
            ans += counter[state ^ (1 << i)]
        counter[state] += 1
    return ans
"-----------------"
test()

