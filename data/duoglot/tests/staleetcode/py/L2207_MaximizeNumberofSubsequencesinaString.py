
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abdcdbc", "ac"]
    # output: 4
    # EXPLANATION:  If we add pattern[0] = 'a' in between text[1] and text[2], we get "ab<u><strong>a</strong></u>dcdbc". Now, the number of times "ac" occurs as a subsequence is 4. Some other strings which have 4 subsequences "ac" after adding a character to text are "<u><strong>a</strong></u>abdcdbc" and "abd<u><strong>a</strong></u>cdbc". However, strings such as "abdc<u><strong>a</strong></u>dbc", "abd<u><strong>c</strong></u>cdbc", and "abdcdbc<u><strong>c</strong></u>", although obtainable, have only 3 subsequences "ac" and are thus suboptimal. It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
    ,
    # example 2
    ["aabb", "ab"]
    # output: 6
    # EXPLANATION:  Some of the strings which can be obtained from text and have 6 subsequences "ab" are "<u><strong>a</strong></u>aabb", "aa<u><strong>a</strong></u>bb", and "aab<u><strong>b</strong></u>b".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumSubsequenceCount 
from collections import Counter
from typing import *
def f_gold(text: str, pattern: str) -> int:
    ans = 0
    cnt = Counter()
    for c in text:
        if c == pattern[1]:
            ans += cnt[pattern[0]]
        cnt[c] += 1
    ans += max(cnt[pattern[0]], cnt[pattern[1]])
    return ans
"-----------------"
test()

