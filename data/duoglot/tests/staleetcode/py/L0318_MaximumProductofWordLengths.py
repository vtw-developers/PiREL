
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]]
    # output: 16
    # EXPLANATION:  The two words can be "abcw", "xtfn".
    ,
    # example 2
    [["a", "ab", "abc", "d", "cd", "bcd", "abcd"]]
    # output: 4
    # EXPLANATION:  The two words can be "ab", "cd".
    ,
    # example 3
    [["a", "aa", "aaa", "aaaa"]]
    # output: 0
    # EXPLANATION:  No such pair of words.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxProduct 
from typing import *
def f_gold(words: List[str]) -> int:
    n = len(words)
    mask = [0] * n
    for i, word in enumerate(words):
        for ch in word:
            mask[i] |= 1 << (ord(ch) - ord('a'))
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mask[i] & mask[j] == 0:
                ans = max(ans, len(words[i]) * len(words[j]))
    return ans
"-----------------"
test()

