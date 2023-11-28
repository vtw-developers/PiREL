
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1+1i", "1+1i"]
    # output: "0+2i"
    # EXPLANATION:  (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
    ,
    # example 2
    ["1+-1i", "1+-1i"]
    # output: "0+-2i"
    # EXPLANATION:  (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### complexNumberMultiply 
from typing import *
def f_gold(num1: str, num2: str) -> str:
    a, b = map(int, num1[:-1].split('+'))
    c, d = map(int, num2[:-1].split('+'))
    return f'{a * c - b * d}+{a * d + c * b}i'
"-----------------"
test()

