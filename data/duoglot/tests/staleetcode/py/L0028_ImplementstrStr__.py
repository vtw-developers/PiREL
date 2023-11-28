
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["hello", "ll"]
    # output: 2
    ,
    # example 2
    ["aaaaa", "bba"]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### strStr 
from typing import *
def f_gold(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle) + 1):
        p = i
        q = 0
        while p < len(haystack) and q < len(needle) and haystack[p] == needle[q]:
            p += 1
            q += 1
        if q == len(needle):
            return i
    return -1
"-----------------"
test()

