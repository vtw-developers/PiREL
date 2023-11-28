
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcacb", "ab", [3, 1, 0]]
    # output: 2
    # EXPLANATION: : After removing the characters at indices 3 and 1, "a<s><strong>b</strong></s>c<s><strong>a</strong></s>cb" becomes "accb". "ab" is a subsequence of "<strong><u>a</u></strong>cc<strong><u>b</u></strong>". If we remove the characters at indices 3, 1, and 0, "<s><strong>ab</strong></s>c<s><strong>a</strong></s>cb" becomes "ccb", and "ab" is no longer a subsequence. Hence, the maximum k is 2.
    ,
    # example 2
    ["abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]]
    # output: 1
    # EXPLANATION: : After removing the character at index 3, "abc<s><strong>b</strong></s>ddddd" becomes "abcddddd". "abcd" is a subsequence of "<u><strong>abcd</strong></u>dddd".
    ,
    # example 3
    ["abcab", "abc", [0, 1, 2, 3, 4]]
    # output: 0
    # EXPLANATION: : If you remove the first index in the array removable, "abc" is no longer a subsequence.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumRemovals 
from typing import *
def f_gold(s: str, p: str, removable: List[int]) -> int:
    def check(k):
        i = j = 0
        ids = set(removable[:k])
        while i < m and j < n:
            if i not in ids and s[i] == p[j]:
                j += 1
            i += 1
        return j == n
    m, n = len(s), len(p)
    left, right = 0, len(removable)
    while left < right:
        mid = (left + right + 1) >> 1
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left
"-----------------"
test()

