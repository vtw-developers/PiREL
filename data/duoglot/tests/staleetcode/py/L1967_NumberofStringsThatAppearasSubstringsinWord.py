
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["a", "abc", "bc", "d"], "abc"]
    # output: 3
    # EXPLANATION:  - "a" appears as a substring in "<u>a</u>bc". - "abc" appears as a substring in "<u>abc</u>". - "bc" appears as a substring in "a<u>bc</u>". - "d" does not appear as a substring in "abc". 3 of the strings in patterns appear as a substring in word.
    ,
    # example 2
    [["a", "b", "c"], "aaaaabbbbb"]
    # output: 2
    # EXPLANATION:  - "a" appears as a substring in "a<u>a</u>aaabbbbb". - "b" appears as a substring in "aaaaabbbb<u>b</u>". - "c" does not appear as a substring in "aaaaabbbbb". 2 of the strings in patterns appear as a substring in word.
    ,
    # example 3
    [["a", "a", "a"], "ab"]
    # output: 3
    # EXPLANATION:  Each of the patterns appears as a substring in word "<u>a</u>b".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numOfStrings 
from typing import *
def f_gold(patterns: List[str], word: str) -> int:
    return sum(1 for p in patterns if p in word)
"-----------------"
test()

