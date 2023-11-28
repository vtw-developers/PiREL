
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 7, 4, 3], 4]
    # output: 13
    # EXPLANATION:  One optimal way to beat the game starting at 13 health is: On round 1, take 2 damage. You have 13 - 2 = 11 health. On round 2, take 7 damage. You have 11 - 7 = 4 health. On round 3, use your armor to protect you from 4 damage. You have 4 - 0 = 4 health. On round 4, take 3 damage. You have 4 - 3 = 1 health. Note that 13 is the minimum health you need to start with to beat the game.
    ,
    # example 2
    [[2, 5, 3, 4], 7]
    # output: 10
    # EXPLANATION:  One optimal way to beat the game starting at 10 health is: On round 1, take 2 damage. You have 10 - 2 = 8 health. On round 2, use your armor to protect you from 5 damage. You have 8 - 0 = 8 health. On round 3, take 3 damage. You have 8 - 3 = 5 health. On round 4, take 4 damage. You have 5 - 4 = 1 health. Note that 10 is the minimum health you need to start with to beat the game.
    ,
    # example 3
    [[3, 3, 3], 0]
    # output: 10
    # EXPLANATION:  One optimal way to beat the game starting at 10 health is: On round 1, take 3 damage. You have 10 - 3 = 7 health. On round 2, take 3 damage. You have 7 - 3 = 4 health. On round 3, take 3 damage. You have 4 - 3 = 1 health. Note that you did not use your armor ability.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumHealth 
from typing import *
def f_gold(damage: List[int], armor: int) -> int:
    return sum(damage) - min(max(damage), armor) + 1
"-----------------"
test()

