
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [9, 3]
    # output: 13
    # EXPLANATION:  You can exchange 3 empty bottles to get 1 full water bottle. Number of water bottles you can drink: 9 + 3 + 1 = 13.
    ,
    # example 2
    [15, 4]
    # output: 19
    # EXPLANATION:  You can exchange 4 empty bottles to get 1 full water bottle.  Number of water bottles you can drink: 15 + 3 + 1 = 19.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numWaterBottles 
from typing import *
def f_gold(numBottles: int, numExchange: int) -> int:
    ans = numBottles
    while numBottles >= numExchange:
        numBottles -= numExchange - 1
        ans += 1
    return ans
"-----------------"
test()

