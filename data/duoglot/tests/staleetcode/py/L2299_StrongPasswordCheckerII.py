
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["IloveLe3tcode!"]
    # output: true
    # EXPLANATION:  The password meets all the requirements. Therefore, we return true.
    ,
    # example 2
    ["Me+You--IsMyDream"]
    # output: false
    # EXPLANATION:  The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
    ,
    # example 3
    ["1aB!"]
    # output: false
    # EXPLANATION:  The password does not meet the length requirement. Therefore, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### strongPasswordCheckerII 
from typing import *
def f_gold(password: str) -> bool:
    if len(password) < 8:
        return False
    ans = 0
    for i, c in enumerate(password):
        if i and password[i - 1] == c:
            return False
        if c.islower():
            ans |= 1
        elif c.isupper():
            ans |= 2
        elif c.isdigit():
            ans |= 4
        else:
            ans |= 8
    return ans == 15
"-----------------"
test()

