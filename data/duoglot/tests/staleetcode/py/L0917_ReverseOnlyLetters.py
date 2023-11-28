
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["ab-cd"]
    # output: "dc-ba"
    ,
    # example 2
    ["a-bC-dEf-ghIj"]
    # output: "j-Ih-gfE-dCba"
    ,
    # example 3
    ["Test1ng-Leet=code-Q!"]
    # output: "Qedo1ct-eeLg=ntse-T!"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseOnlyLetters 
from typing import *
def f_gold(s: str) -> str:
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalpha():
            i += 1
        while i < j and not s[j].isalpha():
            j -= 1
        if i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
    return ''.join(s)
"-----------------"
test()

