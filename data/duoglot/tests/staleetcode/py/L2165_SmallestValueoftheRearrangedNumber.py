
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [310]
    # output: 103
    # EXPLANATION:  The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310.  The arrangement with the smallest value that does not contain any leading zeros is 103.
    ,
    # example 2
    [-7605]
    # output: -7650
    # EXPLANATION:  Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567. The arrangement with the smallest value that does not contain any leading zeros is -7650.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### smallestNumber 
from typing import *
def f_gold(num: int) -> int:
    if num == 0:
        return 0
    cnt = [0] * 10
    neg = num < 0
    num = abs(num)
    while num:
        num, v = divmod(num, 10)
        cnt[v] += 1
    ans = ""
    if neg:
        for i in range(9, -1, -1):
            if cnt[i]:
                ans += str(i) * cnt[i]
        return -int(ans)
    if cnt[0]:
        for i in range(1, 10):
            if cnt[i]:
                ans += str(i)
                cnt[i] -= 1
                break
    for i in range(10):
        if cnt[i]:
            ans += str(i) * cnt[i]
    return int(ans)
"-----------------"
test()

