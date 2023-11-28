
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[197, 130, 1]]
    # output: true
    # EXPLANATION:  data represents the octet sequence: 11000101 10000010 00000001. It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
    ,
    # example 2
    [[235, 140, 4]]
    # output: false
    # EXPLANATION:  data represented the octet sequence: 11101011 10001100 00000100. The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character. The next byte is a continuation byte which starts with 10 and that's correct. But the second continuation byte does not start with 10, so it is invalid.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### validUtf8 
from typing import *
def f_gold(data: List[int]) -> bool:
    n = 0
    for v in data:
        if n > 0:
            if v >> 6 != 0b10:
                return False
            n -= 1
        elif v >> 7 == 0:
            n = 0
        elif v >> 5 == 0b110:
            n = 1
        elif v >> 4 == 0b1110:
            n = 2
        elif v >> 3 == 0b11110:
            n = 3
        else:
            return False
    return n == 0
"-----------------"
test()

