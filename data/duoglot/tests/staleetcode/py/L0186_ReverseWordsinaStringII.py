
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]]
    # output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    ,
    # example 2
    [["a"]]
    # output: ["a"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseWords 
from typing import *
def f_gold(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    def reverse(s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    i, j, n = 0, 0, len(s)
    while j < n:
        if s[j] == ' ':
            reverse(s, i, j - 1)
            i = j + 1
        elif j == n - 1:
            reverse(s, i, j)
        j += 1
    reverse(s, 0, n - 1)
"-----------------"
test()

