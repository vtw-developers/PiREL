
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abcd", "acbd", "aacd"]]
    # output: true
    # EXPLANATION:  Strings "a<strong>b</strong>cd" and "a<strong>a</strong>cd" differ only by one character in the index 1.
    ,
    # example 2
    [["ab", "cd", "yz"]]
    # output: false
    ,
    # example 3
    [["abcd", "cccc", "abyd", "abab"]]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### differByOne 
from typing import *
def f_gold(dict: List[str]) -> bool:
    s = set()
    for word in dict:
        for i in range(len(word)):
            t = word[:i] + "*" + word[i + 1 :]
            if t in s:
                return True
            s.add(t)
    return False
"-----------------"
test()

