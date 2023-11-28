
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: "1"
    # EXPLANATION:  This is the base case.
    ,
    # example 2
    [4]
    # output: "1211"
    # EXPLANATION:  countAndSay(1) = "1" countAndSay(2) = say "1" = one 1 = "11" countAndSay(3) = say "11" = two 1's = "21" countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### countAndSay 
from typing import *
def f_gold(n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        i = 0
        t = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            t.append(str(j - i))
            t.append(str(s[i]))
            i = j
        s = ''.join(t)
    return s
"-----------------"
test()

