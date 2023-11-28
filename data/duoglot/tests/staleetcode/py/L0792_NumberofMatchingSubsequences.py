
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcde", ["a", "bb", "acd", "ace"]]
    # output: 3
    # EXPLANATION:  There are three strings in words that are a subsequence of s: "a", "acd", "ace".
    ,
    # example 2
    ["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numMatchingSubseq 
from collections import defaultdict
from typing import *
def f_gold(s: str, words: List[str]) -> int:
    buckets = defaultdict(list)
    for word in words:
        buckets[word[0]].append(word)
    res = 0
    for c in s:
        old = buckets[c][::1]
        buckets[c].clear()
        for t in old:
            if len(t) == 1:
                res += 1
            else:
                buckets[t[1]].append(t[1:])
    return res
"-----------------"
test()

