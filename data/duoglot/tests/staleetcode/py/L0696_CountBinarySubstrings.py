
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["00110011"]
    # output: 6
    # EXPLANATION:  There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01". Notice that some of these substrings repeat and are counted the number of times they occur. Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    ,
    # example 2
    ["10101"]
    # output: 4
    # EXPLANATION:  There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countBinarySubstrings 
from typing import *
def f_gold(s: str) -> int:
    i, n = 0, len(s)
    t = []
    while i < n:
        cnt = 1
        while i + 1 < n and s[i + 1] == s[i]:
            cnt += 1
            i += 1
        t.append(cnt)
        i += 1
    ans = 0
    for i in range(1, len(t)):
        ans += min(t[i - 1], t[i])
    return ans
"-----------------"
test()

