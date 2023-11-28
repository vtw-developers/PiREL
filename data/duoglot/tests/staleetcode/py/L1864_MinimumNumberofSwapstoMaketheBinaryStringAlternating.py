
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["111000"]
    # output: 1
    # EXPLANATION:  Swap positions 1 and 4: "1<u>1</u>10<u>0</u>0" -> "1<u>0</u>10<u>1</u>0" The string is now alternating.
    ,
    # example 2
    ["010"]
    # output: 0
    # EXPLANATION:  The string is already alternating, no swaps are needed.
    ,
    # example 3
    ["1110"]
    # output: -1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minSwaps 
from typing import *
def f_gold(s: str) -> int:
    s0n0 = s0n1 = s1n0 = s1n1 = 0
    for i in range(len(s)):
        if (i & 1) == 0:
            if s[i] != '0':
                s0n0 += 1
            else:
                s1n1 += 1
        else:
            if s[i] != '0':
                s1n0 += 1
            else:
                s0n1 += 1
    if s0n0 != s0n1 and s1n0 != s1n1:
        return -1
    if s0n0 != s0n1:
        return s1n0
    if s1n0 != s1n1:
        return s0n0
    return min(s0n0, s1n0)
"-----------------"
test()

