
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 4], 2]
    # output: 4
    # EXPLANATION:  Teemo's attacks on Ashe go as follows: - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2. - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5. Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
    ,
    # example 2
    [[1, 2], 2]
    # output: 3
    # EXPLANATION:  Teemo's attacks on Ashe go as follows: - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2. - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3. Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### findPoisonedDuration 
from typing import *
def f_gold(timeSeries: List[int], duration: int) -> int:
    n, res = len(timeSeries), duration
    for i in range(n - 1):
        res += min(duration, timeSeries[i + 1] - timeSeries[i])
    return res
"-----------------"
test()

