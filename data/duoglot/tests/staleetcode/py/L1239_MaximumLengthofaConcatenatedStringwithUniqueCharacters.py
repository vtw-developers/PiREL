
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["un", "iq", "ue"]]
    # output: 4
    # EXPLANATION:  All the valid concatenations are: - "" - "un" - "iq" - "ue" - "uniq" ("un" + "iq") - "ique" ("iq" + "ue") Maximum length is 4.
    ,
    # example 2
    [["cha", "r", "act", "ers"]]
    # output: 6
    # EXPLANATION:  Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
    ,
    # example 3
    [["abcdefghijklmnopqrstuvwxyz"]]
    # output: 26
    # EXPLANATION:  The only string in arr has all 26 characters.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxLength 
from typing import *
def f_gold(arr: List[str]) -> int:
    def ones_count(x):
        c = 0
        while x:
            x &= x - 1
            c += 1
        return c
    ans = 0
    masks = [0]
    for s in arr:
        mask = 0
        for ch in s:
            ch = ord(ch) - ord('a')
            if (mask >> ch) & 1 == 1:
                mask = 0
                break
            mask |= 1 << ch
        if mask == 0:
            continue
        for m in masks:
            if m & mask == 0:
                masks.append(m | mask)
                ans = max(ans, ones_count(m | mask))
    return ans
"-----------------"
test()

