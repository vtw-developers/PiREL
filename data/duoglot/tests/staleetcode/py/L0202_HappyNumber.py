
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [19]
    # output: true
    # EXPLANATION:  1<sup>2</sup> + 9<sup>2</sup> = 82 8<sup>2</sup> + 2<sup>2</sup> = 68 6<sup>2</sup> + 8<sup>2</sup> = 100 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
    ,
    # example 2
    [2]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### isHappy 
from typing import *
def f_gold(n: int) -> bool:
    def get_next(n):
        s = 0
        while n > 0:
            n, digit = divmod(n, 10)
            s += digit**2
        return s
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = get_next(n)
    return n == 1
"-----------------"
test()

