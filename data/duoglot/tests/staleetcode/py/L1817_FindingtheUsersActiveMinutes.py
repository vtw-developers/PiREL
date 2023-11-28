
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5]
    # output: [0,2,0,0,0]
    # EXPLANATION:  The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once). The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2. Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.
    ,
    # example 2
    [[[1, 1], [2, 2], [2, 3]], 4]
    # output: [1,1,0,0]
    # EXPLANATION:  The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1. The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2. There is one user with a UAM of 1 and one with a UAM of 2. Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findingUsersActiveMinutes 
from collections import defaultdict
from typing import *
def f_gold(logs: List[List[int]], k: int) -> List[int]:
    d = defaultdict(set)
    for u, t in logs:
        d[u].add(t)
    ans = [0] * k
    for ts in d.values():
        ans[len(ts) - 1] += 1
    return ans
"-----------------"
test()

