
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ababa"]
    # output: 1
    # EXPLANATION:  s is already a palindrome, so its entirety can be removed in a single step.
    ,
    # example 2
    ["abb"]
    # output: 2
    # EXPLANATION:  "<u>a</u>bb" -> "<u>bb</u>" -> "".  Remove palindromic subsequence "a" then "bb".
    ,
    # example 3
    ["baabb"]
    # output: 2
    # EXPLANATION:  "<u>baa</u>b<u>b</u>" -> "<u>b</u>" -> "".  Remove palindromic subsequence "baab" then "b".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### removePalindromeSub 
from typing import *
def f_gold(s: str) -> int:
    if not s:
        return 0
    if s[::-1] == s:
        return 1
    return 2
"-----------------"
test()

