
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["book"]
    # output: true
    # EXPLANATION:  a = "b<u>o</u>" and b = "<u>o</u>k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
    ,
    # example 2
    ["textbook"]
    # output: false
    # EXPLANATION:  a = "t<u>e</u>xt" and b = "b<u>oo</u>k". a has 1 vowel whereas b has 2. Therefore, they are not alike. Notice that the vowel o is counted twice.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### halvesAreAlike 
from typing import *
def f_gold(s: str) -> bool:
    half = len(s) >> 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s1 = sum(1 for c in s[:half] if c in vowels)
    s2 = sum(1 for c in s[half:] if c in vowels)
    return s1 == s2
"-----------------"
test()

