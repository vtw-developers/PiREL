
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["the sky is blue"]
    # output: "blue is sky the"
    ,
    # example 2
    ["  hello world  "]
    # output: "world hello"
    # EXPLANATION:  Your reversed string should not contain leading or trailing spaces.
    ,
    # example 3
    ["a good   example"]
    # output: "example good a"
    # EXPLANATION:  You need to reduce multiple spaces between two words to a single space in the reversed string.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseWords 
from typing import *
def f_gold(s: str) -> str:
    words = s.strip().split()
    return ' '.join(words[::-1])
"-----------------"
test()

