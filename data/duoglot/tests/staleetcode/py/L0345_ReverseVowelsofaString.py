
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["hello"]
    # output: "holle"
    ,
    # example 2
    ["leetcode"]
    # output: "leotcede"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseVowels 
from typing import *
def f_gold(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    i, j = 0, len(s) - 1
    chars = list(s)
    while i < j:
        if chars[i] not in vowels:
            i += 1
            continue
        if chars[j] not in vowels:
            j -= 1
            continue
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
    return ''.join(chars)
"-----------------"
test()

