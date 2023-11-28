
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    ,
    # example 2
    [9]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### readBinaryWatch 
from typing import *
def f_gold(turnedOn: int) -> List[str]:
    return [
        '{:d}:{:02d}'.format(i, j)
        for i in range(12)
        for j in range(60)
        if (bin(i) + bin(j)).count('1') == turnedOn
    ]
"-----------------"
test()

