
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 4, 2, 3, 4, 7]]
    # output: 4
    # EXPLANATION:  We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
    ,
    # example 2
    [[1, 0, 5, 3]]
    # output: -1
    # EXPLANATION:  There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumCardPickup 
from typing import *
def f_gold(cards: List[int]) -> int:
    m = {}
    ans = 10**6
    for i, c in enumerate(cards):
        if c in m:
            ans = min(ans, i - m[c] + 1)
        m[c] = i
    return -1 if ans == 10**6 else ans
"-----------------"
test()

