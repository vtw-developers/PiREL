
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["ant", "act", "tack"], ["tack", "act", "acti"]]
    # output: 2
    # EXPLANATION:  - In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack". - There is no string in startWords that can be used to obtain targetWords[1] = "act".   Note that "act" does exist in startWords, but we <strong>must</strong> append one letter to the string before rearranging it. - In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
    ,
    # example 2
    [["ab", "a"], ["abc", "abcd"]]
    # output: 1
    # EXPLANATION:  - In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc". - There is no string in startWords that can be used to obtain targetWords[1] = "abcd".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### wordCount 
from typing import *
def f_gold(startWords: List[str], targetWords: List[str]) -> int:
    s = set()
    for word in startWords:
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        s.add(mask)
    ans = 0
    for word in targetWords:
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        for c in word:
            t = mask ^ (1 << (ord(c) - ord('a')))
            if t in s:
                ans += 1
                break
    return ans
"-----------------"
test()

