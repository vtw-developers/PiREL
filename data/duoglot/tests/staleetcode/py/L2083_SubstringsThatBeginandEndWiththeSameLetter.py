
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcba"]
    # output: 7
    # EXPLANATION:  The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a". The substring of length 3 that starts and ends with the same letter is: "bcb". The substring of length 5 that starts and ends with the same letter is: "abcba".
    ,
    # example 2
    ["abacad"]
    # output: 9
    # EXPLANATION:  The substrings of length 1 that start and end with the same letter are: "a", "b", "a", "c", "a", and "d". The substrings of length 3 that start and end with the same letter are: "aba" and "aca". The substring of length 5 that starts and ends with the same letter is: "abaca".
    ,
    # example 3
    ["a"]
    # output: 1
    # EXPLANATION:  The substring of length 1 that starts and ends with the same letter is: "a".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfSubstrings 
from typing import *
def f_gold(s: str) -> int:
    counter = [0] * 26
    ans = 0
    for c in s:
        i = ord(c) - ord('a')
        counter[i] += 1
        ans += counter[i]
    return ans
"-----------------"
test()

