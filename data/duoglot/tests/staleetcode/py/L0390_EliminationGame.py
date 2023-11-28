
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [9]
    # output: 6
    # EXPLANATION:  arr = [<u>1</u>, 2, <u>3</u>, 4, <u>5</u>, 6, <u>7</u>, 8, <u>9</u>] arr = [2, <u>4</u>, 6, <u>8</u>] arr = [<u>2</u>, 6] arr = [6]
    ,
    # example 2
    [1]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lastRemaining 
from typing import *
def f_gold(n: int) -> int:
    a1, an = 1, n
    i, step, cnt = 0, 1, n
    while cnt > 1:
        if i % 2:
            an -= step
            if cnt % 2:
                a1 += step
        else:
            a1 += step
            if cnt % 2:
                an -= step
        cnt >>= 1
        step <<= 1
        i += 1
    return a1
"-----------------"
test()

