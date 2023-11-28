
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["2?:?0"]
    # output: "23:50"
    # EXPLANATION:  The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
    ,
    # example 2
    ["0?:3?"]
    # output: "09:39"
    ,
    # example 3
    ["1?:22"]
    # output: "19:22"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maximumTime 
from typing import *
def f_gold(time: str) -> str:
    t = list(time)
    if t[0] == '?':
        t[0] = '1' if '4' <= t[1] <= '9' else '2'
    if t[1] == '?':
        t[1] = '3' if t[0] == '2' else '9'
    if t[3] == '?':
        t[3] = '5'
    if t[4] == '?':
        t[4] = '9'
    return ''.join(t)
"-----------------"
test()

