
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 4, 3], [2, 3, 1]]
    # output: 9
    # EXPLANATION:  The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms. One optimal way is: On day 0, plant the 0<sup>th</sup> seed. The seed grows for 2 full days and blooms on day 3. On days 1, 2, 3, and 4, plant the 1<sup>st</sup> seed. The seed grows for 3 full days and blooms on day 8. On days 5, 6, and 7, plant the 2<sup>nd</sup> seed. The seed grows for 1 full day and blooms on day 9. Thus, on day 9, all the seeds are blooming.
    ,
    # example 2
    [[1, 2, 3, 2], [2, 1, 2, 1]]
    # output: 9
    # EXPLANATION:  The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms. One optimal way is: On day 1, plant the 0<sup>th</sup> seed. The seed grows for 2 full days and blooms on day 4. On days 0 and 3, plant the 1<sup>st</sup> seed. The seed grows for 1 full day and blooms on day 5. On days 2, 4, and 5, plant the 2<sup>nd</sup> seed. The seed grows for 2 full days and blooms on day 8. On days 6 and 7, plant the 3<sup>rd</sup> seed. The seed grows for 1 full day and blooms on day 9. Thus, on day 9, all the seeds are blooming.
    ,
    # example 3
    [[1], [1]]
    # output: 2
    # EXPLANATION:  On day 0, plant the 0<sup>th</sup> seed. The seed grows for 1 full day and blooms on day 2. Thus, on day 2, all the seeds are blooming.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### earliestFullBloom 
from typing import *
def f_gold(plantTime: List[int], growTime: List[int]) -> int:
    ans = t = 0
    for a, b in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
        t += a
        ans = max(ans, t + b)
    return ans
"-----------------"
test()

