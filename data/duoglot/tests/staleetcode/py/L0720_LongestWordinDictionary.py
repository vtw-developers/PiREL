
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["w", "wo", "wor", "worl", "world"]]
    # output: "world"
    # EXPLANATION:  The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
    ,
    # example 2
    [["a", "banana", "app", "appl", "ap", "apply", "apple"]]
    # output: "apple"
    # EXPLANATION:  Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### longestWord 
from typing import *
def f_gold(words: List[str]) -> str:
    cnt, ans = 0, ''
    s = set(words)
    for w in s:
        n = len(w)
        if all(w[:i] in s for i in range(1, n)):
            if cnt < n:
                cnt, ans = n, w
            elif cnt == n and w < ans:
                ans = w
    return ans
"-----------------"
test()

