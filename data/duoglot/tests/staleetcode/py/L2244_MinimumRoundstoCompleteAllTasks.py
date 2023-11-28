
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]]
    # output: 4
    # EXPLANATION:  To complete all the tasks, a possible plan is: - In the first round, you complete 3 tasks of difficulty level 2.  - In the second round, you complete 2 tasks of difficulty level 3.  - In the third round, you complete 3 tasks of difficulty level 4.  - In the fourth round, you complete 2 tasks of difficulty level 4.   It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
    ,
    # example 2
    [[2, 3, 3]]
    # output: -1
    # EXPLANATION:  There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### minimumRounds 
from collections import Counter
from typing import *
def f_gold(tasks: List[int]) -> int:
    cnt = Counter(tasks)
    mi = min(cnt.values())
    if mi == 1:
        return -1
    return sum(v // 3 + (0 if v % 3 == 0 else 1) for v in cnt.values())
"-----------------"
test()

