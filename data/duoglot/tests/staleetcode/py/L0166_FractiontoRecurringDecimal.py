
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2]
    # output: "0.5"
    ,
    # example 2
    [2, 1]
    # output: "2"
    ,
    # example 3
    [4, 333]
    # output: "0.(012)"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### fractionToDecimal 
from typing import *
def f_gold(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return '0'
    res = []
    neg = (numerator > 0) ^ (denominator > 0)
    if neg:
        res.append('-')
    num, d = abs(numerator), abs(denominator)
    res.append(str(num // d))
    num %= d
    if num == 0:
        return ''.join(res)
    res.append('.')
    mp = {}
    while num != 0:
        mp[num] = len(res)
        num *= 10
        res.append(str(num // d))
        num %= d
        if num in mp:
            idx = mp[num]
            res.insert(idx, '(')
            res.append(')')
            break
    return ''.join(res)
"-----------------"
test()

