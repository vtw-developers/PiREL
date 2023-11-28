
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["abcdefd", "d"]
    # output: "<u>dcba</u>efd"
    # EXPLANATION:  The first occurrence of "d" is at index 3.  Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
    ,
    # example 2
    ["xyxzxe", "z"]
    # output: "<u>zxyx</u>xe"
    # EXPLANATION:  The first and only occurrence of "z" is at index 3. Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
    ,
    # example 3
    ["abcd", "z"]
    # output: "abcd"
    # EXPLANATION:  "z" does not exist in word. You should not do any reverse operation, the resulting string is "abcd".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reversePrefix 
from typing import *
def f_gold(word: str, ch: str) -> str:
    i = word.find(ch)
    return word if i == -1 else word[i::-1] + word[i + 1 :]
"-----------------"
test()

