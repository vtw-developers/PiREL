
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2736]
    # output: 7236
    # EXPLANATION:  Swap the number 2 and the number 7.
    ,
    # example 2
    [9973]
    # output: 9973
    # EXPLANATION:  No swap.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumSwap 
from typing import *
def f_gold(num: int) -> int:
    chars = list(str(num))
    n = len(chars)
    for i in range(n - 1):
        mx = i + 1
        for j in range(i + 1, n):
            if ord(chars[j]) >= ord(chars[mx]):
                mx = j
        if ord(chars[i]) < ord(chars[mx]):
            chars[i], chars[mx] = chars[mx], chars[i]
            break
    return int(''.join(chars))
"-----------------"
test()

