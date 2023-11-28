
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [121]
    # output: true
    # EXPLANATION:  121 reads as 121 from left to right and from right to left.
    ,
    # example 2
    [-121]
    # output: false
    # EXPLANATION:  From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    ,
    # example 3
    [10]
    # output: false
    # EXPLANATION:  Reads 01 from right to left. Therefore it is not a palindrome.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isPalindrome 
from typing import *
def f_gold(x: int) -> bool:
    if x < 0:
        return False
    y, t = 0, x
    while t:
        y = y * 10 + t % 10
        t //= 10
    return x == y
"-----------------"
test()

