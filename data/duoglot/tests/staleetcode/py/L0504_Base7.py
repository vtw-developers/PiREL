
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [100]
    # output: "202"
    ,
    # example 2
    [-7]
    # output: "-10"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### convertToBase7 
from typing import *
def f_gold(num: int) -> str:
    if num == 0:
        return '0'
    if num < 0:
        return '-' + f_gold(-num)
    ans = []
    while num:
        ans.append(str(num % 7))
        num //= 7
    return ''.join(ans[::-1])
"-----------------"
test()

