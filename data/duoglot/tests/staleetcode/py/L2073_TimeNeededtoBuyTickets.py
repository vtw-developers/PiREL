
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 2], 2]
    # output: 6
    # EXPLANATION:   - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1]. - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0]. The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
    ,
    # example 2
    [[5, 1, 1, 1], 0]
    # output: 8
    # EXPLANATION:  - In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0]. - In the next 4 passes, only the person in position 0 is buying tickets. The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### timeRequiredToBuy 
from typing import *
def f_gold(tickets: List[int], k: int) -> int:
    ans = 0
    for i, t in enumerate(tickets):
        if i <= k:
            ans += min(tickets[k], t)
        else:
            ans += min(tickets[k] - 1, t)
    return ans
"-----------------"
test()

