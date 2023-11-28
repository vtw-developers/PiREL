
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[16, 16]]
    # output: 2
    # EXPLANATION:  2 people friend request each other.
    ,
    # example 2
    [[16, 17, 18]]
    # output: 2
    # EXPLANATION:  Friend requests are made 17 -> 16, 18 -> 17.
    ,
    # example 3
    [[20, 30, 100, 110, 120]]
    # output: 3
    # EXPLANATION:  Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numFriendRequests 
from collections import Counter
from typing import *
def f_gold(ages: List[int]) -> int:
    counter = Counter(ages)
    ans = 0
    for i in range(1, 121):
        n1 = counter[i]
        for j in range(1, 121):
            n2 = counter[j]
            if not (j <= 0.5 * i + 7 or j > i or (j > 100 and i < 100)):
                ans += n1 * n2
                if i == j:
                    ans -= n2
    return ans
"-----------------"
test()

