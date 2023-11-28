
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 90], 3]
    # output: [101,111,121,131,141,999]
    # EXPLANATION:  The first few palindromes of length 3 are: 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ... The 90<sup>th</sup> palindrome of length 3 is 999.
    ,
    # example 2
    [[2, 4, 6], 4]
    # output: [1111,1331,1551]
    # EXPLANATION:  The first six palindromes of length 4 are: 1001, 1111, 1221, 1331, 1441, and 1551.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### kthPalindrome 
from typing import *
def f_gold(queries: List[int], intLength: int) -> List[int]:
    l = (intLength + 1) >> 1
    start, end = 10 ** (l - 1), 10**l - 1
    ans = []
    for q in queries:
        v = start + q - 1
        if v > end:
            ans.append(-1)
            continue
        s = str(v)
        s += s[::-1][intLength % 2 :]
        ans.append(int(s))
    return ans
"-----------------"
test()

