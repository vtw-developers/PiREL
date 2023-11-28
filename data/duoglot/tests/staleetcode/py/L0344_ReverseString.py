
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["h", "e", "l", "l", "o"]]
    # output: ["o","l","l","e","h"]
    ,
    # example 2
    [["H", "a", "n", "n", "a", "h"]]
    # output: ["h","a","n","n","a","H"]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### reverseString 
from typing import *
def f_gold(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]
"-----------------"
test()

