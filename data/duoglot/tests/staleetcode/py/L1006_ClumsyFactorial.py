
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 7
    # EXPLANATION:  7 = 4 * 3 / 2 + 1
    ,
    # example 2
    [10]
    # output: 12
    # EXPLANATION:  12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### clumsy 
from typing import *
def f_gold(N: int) -> int:
    op = 0
    s = [N]
    for i in range(N - 1, 0, -1):
        if op == 0:
            s.append(s.pop() * i)
        elif op == 1:
            s.append(int(s.pop() / i))
        elif op == 2:
            s.append(i)
        else:
            s.append(-i)
        op = (op + 1) % 4
    return sum(s)
"-----------------"
test()

