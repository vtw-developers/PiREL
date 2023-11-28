
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab", "eidbaooo"]
    # output: true
    # EXPLANATION:  s2 contains one permutation of s1 ("ba").
    ,
    # example 2
    ["ab", "eidboaoo"]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### checkInclusion 
from typing import *
def f_gold(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        return False
    flag1 = [0] * 26
    flag2 = [0] * 26
    for i, x in enumerate(s1):
        flag1[ord(x) - ord('a')] += 1
    for i, x in enumerate(s2):
        flag2[ord(x) - ord('a')] += 1
        if i >= len(s1):
            flag2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        if flag1 == flag2:
            return True
    return False
"-----------------"
test()

