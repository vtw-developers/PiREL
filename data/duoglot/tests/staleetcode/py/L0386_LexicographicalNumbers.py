
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [13]
    # output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
    ,
    # example 2
    [2]
    # output: [1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lexicalOrder 
from typing import *
def f_gold(n: int) -> List[int]:
    v = 1
    ans = []
    for i in range(n):
        ans.append(v)
        if v * 10 <= n:
            v *= 10
        else:
            while v % 10 == 9 or v + 1 > n:
                v //= 10
            v += 1
    return ans
"-----------------"
test()

