
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["l|*e*et|c**o|*de|"]
    # output: 2
    # EXPLANATION:  The considered characters are underlined: "<u>l</u>|*e*et|<u>c**o</u>|*de|". The characters between the first and second '|' are excluded from the answer. Also, the characters between the third and fourth '|' are excluded from the answer. There are 2 asterisks considered. Therefore, we return 2.
    ,
    # example 2
    ["iamprogrammer"]
    # output: 0
    # EXPLANATION:  In this example, there are no asterisks in s. Therefore, we return 0.
    ,
    # example 3
    ["yo|uar|e**|b|e***au|tifu|l"]
    # output: 5
    # EXPLANATION:  The considered characters are underlined: "<u>yo</u>|uar|<u>e**</u>|b|<u>e***au</u>|tifu|<u>l</u>". There are 5 asterisks considered. Therefore, we return 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countAsterisks 
from typing import *
def f_gold(s: str) -> int:
    ans = t = 0
    for c in s:
        if c == '|':
            t ^= 1
        elif c == '*':
            if t == 0:
                ans += 1
    return ans
"-----------------"
test()

