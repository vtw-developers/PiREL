
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["09:31", "10:14"]
    # output: 1
    # EXPLANATION:  You played one full round from 09:45 to 10:00. You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it began. You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it ended.
    ,
    # example 2
    ["21:30", "03:00"]
    # output: 22
    # EXPLANATION:  You played 10 full rounds from 21:30 to 00:00 and 12 full rounds from 00:00 to 03:00. 10 + 12 = 22.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfRounds 
from typing import *
def f_gold(startTime: str, finishTime: str) -> int:
    def get(s: str) -> int:
        return int(s[:2]) * 60 + int(s[3:])
    start, finish = get(startTime), get(finishTime)
    if start > finish:
        finish += 24 * 60
    start, finish = (start + 14) // 15, finish // 15
    return max(0, finish - start)
"-----------------"
test()

