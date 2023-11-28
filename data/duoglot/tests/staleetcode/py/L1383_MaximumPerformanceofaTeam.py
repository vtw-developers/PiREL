
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2]
    # output: 60
    # EXPLANATION:   We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
    ,
    # example 2
    [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3]
    # output: 68
    # EXPLANATION: This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
    ,
    # example 3
    [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4]
    # output: 72
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxPerformance 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(n: int, speed: List[int], efficiency: List[int], k: int
) -> int:
    team = [(s, e) for s, e in zip(speed, efficiency)]
    team.sort(key=lambda x: -x[1])
    q = []
    t = 0
    ans = 0
    mod = int(1e9) + 7
    for s, e in team:
        t += s
        ans = max(ans, t * e)
        heappush(q, s)
        if len(q) >= k:
            t -= heappop(q)
    return ans % mod
"-----------------"
test()

