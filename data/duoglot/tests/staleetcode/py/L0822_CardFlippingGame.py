
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 4, 4, 7], [1, 3, 4, 1, 3]]
    # output: 2
    # EXPLANATION:  If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3]. 2 is the minimum good integer as it appears facing down but not facing up. It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.
    ,
    # example 2
    [[1], [1]]
    # output: 0
    # EXPLANATION:  There are no good integers no matter how we flip the cards, so we return 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### flipgame 
from itertools import chain
from typing import *
def f_gold(fronts: List[int], backs: List[int]) -> int:
    same = {a for a, b in zip(fronts, backs) if a == b}
    ans = 9999
    for x in chain(fronts, backs):
        if x not in same:
            ans = min(ans, x)
    return ans % 9999
"-----------------"
test()

