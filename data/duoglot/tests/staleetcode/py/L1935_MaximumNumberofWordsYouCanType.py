
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["hello world", "ad"]
    # output: 1
    # EXPLANATION:  We cannot type "world" because the 'd' key is broken.
    ,
    # example 2
    ["leet code", "lt"]
    # output: 1
    # EXPLANATION:  We cannot type "leet" because the 'l' and 't' keys are broken.
    ,
    # example 3
    ["leet code", "e"]
    # output: 0
    # EXPLANATION:  We cannot type either word because the 'e' key is broken.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### canBeTypedWords 
from typing import *
def f_gold(text: str, brokenLetters: str) -> int:
    letters = set(brokenLetters)
    res = 0
    for word in text.split():
        find = False
        for letter in letters:
            if letter in word:
                find = True
                break
        if not find:
            res += 1
    return res
"-----------------"
test()

