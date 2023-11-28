
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["cczazcc", 3]
    # output: "zzcccac"
    # EXPLANATION:  We use all of the characters from s to construct the repeatLimitedString "zzcccac". The letter 'a' appears at most 1 time in a row. The letter 'c' appears at most 3 times in a row. The letter 'z' appears at most 2 times in a row. Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString. The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac". Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
    ,
    # example 2
    ["aababab", 2]
    # output: "bbabaa"
    # EXPLANATION:  We use only some of the characters from s to construct the repeatLimitedString "bbabaa".  The letter 'a' appears at most 2 times in a row. The letter 'b' appears at most 2 times in a row. Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString. The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa". Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### repeatLimitedString 
from typing import *
def f_gold(s: str, repeatLimit: int) -> str:
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    ans = []
    for i in range(25, -1, -1):
        j = i - 1
        while 1:
            for _ in range(min(repeatLimit, cnt[i])):
                cnt[i] -= 1
                ans.append(chr(ord('a') + i))
            if cnt[i] == 0:
                break
            while j >= 0 and cnt[j] == 0:
                j -= 1
            if j < 0:
                break
            cnt[j] -= 1
            ans.append(chr(ord('a') + j))
    return ''.join(ans)
"-----------------"
test()

