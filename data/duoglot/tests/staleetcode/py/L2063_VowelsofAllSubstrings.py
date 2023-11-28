
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["aba"]
    # output: 6
    # EXPLANATION:   All possible substrings are: "a", "ab", "aba", "b", "ba", and "a". - "b" has 0 vowels in it - "a", "ab", "ba", and "a" have 1 vowel each - "aba" has 2 vowels in it Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.
    ,
    # example 2
    ["abc"]
    # output: 3
    # EXPLANATION:   All possible substrings are: "a", "ab", "abc", "b", "bc", and "c". - "a", "ab", and "abc" have 1 vowel each - "b", "bc", and "c" have 0 vowels each Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
    ,
    # example 3
    ["ltcd"]
    # output: 0
    # EXPLANATION:  There are no vowels in any substring of "ltcd".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countVowels 
from typing import *
def f_gold(word: str) -> int:
    ans, n = 0, len(word)
    for i, c in enumerate(word):
        if c in ['a', 'e', 'i', 'o', 'u']:
            ans += (i + 1) * (n - i)
    return ans
"-----------------"
test()

