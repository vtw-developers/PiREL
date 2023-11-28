
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [153]
    # output: true
    # EXPLANATION:  153 is a 3-digit number, and 153 = 1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup>.
    ,
    # example 2
    [123]
    # output: false
    # EXPLANATION:  123 is a 3-digit number, and 123 != 1<sup>3</sup> + 2<sup>3</sup> + 3<sup>3</sup> = 36.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isArmstrong 
from typing import *
def f_gold(n: int) -> bool:
    k = len(str(n))
    s, t = 0, n
    while t:
        t, v = divmod(t, 10)
        s += pow(v, k)
    return n == s
"-----------------"
test()

