
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["bella", "label", "roller"]]
    # output: ["e","l","l"]
    ,
    # example 2
    [["cool", "lock", "cook"]]
    # output: ["c","o"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### commonChars 
from typing import *
def f_gold(words: List[str]) -> List[str]:
    freq = [10000] * 26
    for word in words:
        t = [0] * 26
        for c in word:
            t[ord(c) - ord('a')] += 1
        for i in range(26):
            freq[i] = min(freq[i], t[i])
    res = []
    for i in range(26):
        if freq[i] > 0:
            res.extend([chr(i + ord("a"))] * freq[i])
    return res
"-----------------"
test()

