
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["1101"]
    # output: 6
    # EXPLANATION:  "1101" corressponds to number 13 in their decimal representation. Step 1) 13 is odd, add 1 and obtain 14.  Step 2) 14 is even, divide by 2 and obtain 7. Step 3) 7 is odd, add 1 and obtain 8. Step 4) 8 is even, divide by 2 and obtain 4.   Step 5) 4 is even, divide by 2 and obtain 2.  Step 6) 2 is even, divide by 2 and obtain 1. 
    ,
    # example 2
    ["10"]
    # output: 1
    # EXPLANATION:  "10" corressponds to number 2 in their decimal representation. Step 1) 2 is even, divide by 2 and obtain 1. 
    ,
    # example 3
    ["1"]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numSteps 
from typing import *
def f_gold(s: str) -> int:
    carry = False
    ans = 0
    for c in s[:0:-1]:
        if carry:
            if c == '0':
                c = '1'
                carry = False
            else:
                c = '0'
        if c == '1':
            ans += 1
            carry = True
        ans += 1
    if carry:
        ans += 1
    return ans
"-----------------"
test()

