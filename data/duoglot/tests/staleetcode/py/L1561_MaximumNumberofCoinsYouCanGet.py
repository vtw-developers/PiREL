
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 1, 2, 7, 8]]
    # output: 9
    # EXPLANATION: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with <strong>7</strong> coins and Bob the last one. Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with <strong>2</strong> coins and Bob the last one. The maximum number of coins which you can have are: 7 + 2 = 9. On the other hand if we choose this arrangement (1, <strong>2</strong>, 8), (2, <strong>4</strong>, 7) you only get 2 + 4 = 6 coins which is not optimal.
    ,
    # example 2
    [[2, 4, 5]]
    # output: 4
    ,
    # example 3
    [[9, 8, 7, 6, 5, 1, 2, 3, 4]]
    # output: 18
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxCoins 
from typing import *
def f_gold(piles: List[int]) -> int:
    piles.sort()
    return sum(piles[-2 : len(piles) // 3 - 1 : -2])
"-----------------"
test()

