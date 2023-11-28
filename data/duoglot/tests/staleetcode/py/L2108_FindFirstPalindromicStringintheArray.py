
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abc", "car", "ada", "racecar", "cool"]]
    # output: "ada"
    # EXPLANATION:  The first string that is palindromic is "ada". Note that "racecar" is also palindromic, but it is not the first.
    ,
    # example 2
    [["notapalindrome", "racecar"]]
    # output: "racecar"
    # EXPLANATION:  The first and only string that is palindromic is "racecar".
    ,
    # example 3
    [["def", "ghi"]]
    # output: ""
    # EXPLANATION:  There are no palindromic strings, so the empty string is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### firstPalindrome 
from typing import *
def f_gold(words: List[str]) -> str:
    def check(s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    for word in words:
        if check(word):
            return word
    return ''
"-----------------"
test()

