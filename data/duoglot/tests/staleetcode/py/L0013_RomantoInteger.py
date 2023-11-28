
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["III"]
    # output: 3
    # EXPLANATION:  III = 3.
    ,
    # example 2
    ["LVIII"]
    # output: 58
    # EXPLANATION:  L = 50, V= 5, III = 3.
    ,
    # example 3
    ["MCMXCIV"]
    # output: 1994
    # EXPLANATION:  M = 1000, CM = 900, XC = 90 and IV = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### romanToInt 
from typing import *
def f_gold(s: str) -> int:
    nums = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    i = res = 0
    while i < len(s):
        if i + 1 < len(s) and s[i : i + 2] in nums:
            res += nums[s[i : i + 2]]
            i += 2
        else:
            res += nums[s[i : i + 1]]
            i += 1
    return res
"-----------------"
test()

