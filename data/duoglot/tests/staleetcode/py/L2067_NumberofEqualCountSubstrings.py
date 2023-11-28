
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aaabcbbcc", 3]
    # output: 3
    # EXPLANATION:  The substring that starts at index 0 and ends at index 2 is "aaa". The letter 'a' in the substring appears exactly 3 times. The substring that starts at index 3 and ends at index 8 is "bcbbcc". The letters 'b' and 'c' in the substring appear exactly 3 times. The substring that starts at index 0 and ends at index 8 is "aaabcbbcc". The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
    ,
    # example 2
    ["abcd", 2]
    # output: 0
    # EXPLANATION:  The number of times each letter appears in s is less than count. Therefore, no substrings in s are equal count substrings, so return 0.
    ,
    # example 3
    ["a", 5]
    # output: 0
    # EXPLANATION:  The number of times each letter appears in s is less than count. Therefore, no substrings in s are equal count substrings, so return 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### equalCountSubstrings 
from typing import *
def f_gold(s: str, count: int) -> int:
    n = len(s)
    if count > n:
        return 0
    counter = [[0] * 26 for _ in range(n + 1)]
    def check(i, j):
        c1 = counter[i]
        c2 = counter[j + 1]
        for k in range(26):
            if c2[k] == 0 or c1[k] == c2[k]:
                continue
            if c2[k] - c1[k] != count:
                return False
        return True
    ans = 0
    for i, c in enumerate(s):
        idx = ord(c) - ord('a')
        for j in range(26):
            counter[i + 1][j] = counter[i][j]
        counter[i + 1][idx] = counter[i][idx] + 1
        l = 0
        for _ in range(26):
            l += count
            j = i - l + 1
            if j < 0:
                break
            ans += check(j, i)
    return ans
"-----------------"
test()

