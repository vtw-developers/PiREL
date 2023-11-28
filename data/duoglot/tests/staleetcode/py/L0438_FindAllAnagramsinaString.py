
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["cbaebabacd", "abc"]
    # output: [0,6]
    # EXPLANATION:  The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".
    ,
    # example 2
    ["abab", "ab"]
    # output: [0,1,2]
    # EXPLANATION:  The substring with start index = 0 is "ab", which is an anagram of "ab". The substring with start index = 1 is "ba", which is an anagram of "ab". The substring with start index = 2 is "ab", which is an anagram of "ab".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findAnagrams 
from collections import Counter
from typing import *
def f_gold(s: str, p: str) -> List[int]:
    counter = Counter(p)
    ans = []
    left = right = 0
    t = Counter()
    while right < len(s):
        t[s[right]] += 1
        while t[s[right]] > counter[s[right]]:
            t[s[left]] -= 1
            left += 1
        if right - left + 1 == len(p):
            ans.append(left)
        right += 1
    return ans
"-----------------"
test()

