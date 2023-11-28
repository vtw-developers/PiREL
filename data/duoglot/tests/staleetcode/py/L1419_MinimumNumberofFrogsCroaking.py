
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["croakcroak"]
    # output: 1
    # EXPLANATION:  One frog yelling "croak<strong>"</strong> twice.
    ,
    # example 2
    ["crcoakroak"]
    # output: 2
    # EXPLANATION:  The minimum number of frogs is two.  The first frog could yell "<strong>cr</strong>c<strong>oak</strong>roak". The second frog could yell later "cr<strong>c</strong>oak<strong>roak</strong>".
    ,
    # example 3
    ["croakcrook"]
    # output: -1
    # EXPLANATION:  The given string is an invalid combination of "croak<strong>"</strong> from different frogs.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minNumberOfFrogs 
from typing import *
def f_gold(croakOfFrogs: str) -> int:
    c = r = o = a = k = ans = 0
    for ch in croakOfFrogs:
        if ch == 'c':
            c += 1
            if k > 0:
                k -= 1
            else:
                ans += 1
        elif ch == 'r':
            r += 1
            c -= 1
        elif ch == 'o':
            o += 1
            r -= 1
        elif ch == 'a':
            a += 1
            o -= 1
        else:
            k += 1
            a -= 1
        if c < 0 or r < 0 or o < 0 or a < 0:
            return -1
    return -1 if c != 0 or r != 0 or o != 0 or a != 0 else ans
"-----------------"
test()

