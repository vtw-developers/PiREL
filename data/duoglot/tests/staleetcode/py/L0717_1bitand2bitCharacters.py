
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 0]]
    # output: true
    # EXPLANATION:  The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
    ,
    # example 2
    [[1, 1, 1, 0]]
    # output: false
    # EXPLANATION:  The only way to decode it is two-bit character and two-bit character. So the last character is not one-bit character.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isOneBitCharacter 
from typing import *
def f_gold(bits: List[int]) -> bool:
    i, n = 0, len(bits)
    while i < n - 1:
        i += bits[i] + 1
    return i == n - 1
"-----------------"
test()

