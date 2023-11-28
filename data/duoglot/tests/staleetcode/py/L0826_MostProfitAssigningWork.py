
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]]
    # output: 100
    # EXPLANATION:  Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
    ,
    # example 2
    [[85, 47, 57], [24, 66, 99], [40, 25, 25]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### maxProfitAssignment 
from typing import *
def f_gold(difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    n = len(difficulty)
    job = [(difficulty[i], profit[i]) for i in range(n)]
    job.sort(key=lambda x: x[0])
    worker.sort()
    i = t = res = 0
    for w in worker:
        while i < n and job[i][0] <= w:
            t = max(t, job[i][1])
            i += 1
        res += t
    return res
"-----------------"
test()

