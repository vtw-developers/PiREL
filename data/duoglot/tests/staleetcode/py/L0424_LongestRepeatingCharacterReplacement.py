
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ABAB", 2]
    # output: 4
    # EXPLANATION:  Replace the two 'A's with two 'B's or vice versa.
    ,
    # example 2
    ["AABABBA", 1]
    # output: 4
    # EXPLANATION:  Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### characterReplacement 
from typing import *
def f_gold(s: str, k: int) -> int:
    counter = [0] * 26
    i = j = maxCnt = 0
    while i < len(s):
        counter[ord(s[i]) - ord('A')] += 1
        maxCnt = max(maxCnt, counter[ord(s[i]) - ord('A')])
        if i - j + 1 > maxCnt + k:
            counter[ord(s[j]) - ord('A')] -= 1
            j += 1
        i += 1
    return i - j
"-----------------"
test()

