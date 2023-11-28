
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["a1c1e1"]
    # output: "abcdef"
    # EXPLANATION: The digits are replaced as follows: - s[1] -> shift('a',1) = 'b' - s[3] -> shift('c',1) = 'd' - s[5] -> shift('e',1) = 'f'
    ,
    # example 2
    ["a1b2c3d4e"]
    # output: "abbdcfdhe"
    # EXPLANATION: The digits are replaced as follows: - s[1] -> shift('a',1) = 'b' - s[3] -> shift('b',2) = 'd' - s[5] -> shift('c',3) = 'f' - s[7] -> shift('d',4) = 'h'
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### replaceDigits 
from typing import *
def f_gold(s: str) -> str:
    s = list(s)
    for i in range(1, len(s), 2):
        s[i] = chr(ord(s[i - 1]) + int(s[i]))
    return ''.join(s)
"-----------------"
test()

