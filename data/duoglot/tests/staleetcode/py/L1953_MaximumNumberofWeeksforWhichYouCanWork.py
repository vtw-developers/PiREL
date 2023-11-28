
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 6
    # EXPLANATION:  One possible scenario is:     - During the 1<sup>st</sup> week, you will work on a milestone of project 0. - During the 2<sup>nd</sup> week, you will work on a milestone of project 2. - During the 3<sup>rd</sup> week, you will work on a milestone of project 1. - During the 4<sup>th</sup> week, you will work on a milestone of project 2. - During the 5<sup>th</sup> week, you will work on a milestone of project 1. - During the 6<sup>th</sup> week, you will work on a milestone of project 2. The total number of weeks is 6.
    ,
    # example 2
    [[5, 2, 1]]
    # output: 7
    # EXPLANATION:  One possible scenario is: - During the 1<sup>st</sup> week, you will work on a milestone of project 0. - During the 2<sup>nd</sup> week, you will work on a milestone of project 1. - During the 3<sup>rd</sup> week, you will work on a milestone of project 0. - During the 4<sup>th</sup> week, you will work on a milestone of project 1. - During the 5<sup>th</sup> week, you will work on a milestone of project 0. - During the 6<sup>th</sup> week, you will work on a milestone of project 2. - During the 7<sup>th</sup> week, you will work on a milestone of project 0. The total number of weeks is 7. Note that you cannot work on the last milestone of project 0 on 8<sup>th</sup> week because it would violate the rules. Thus, one milestone in project 0 will remain unfinished.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### numberOfWeeks 
from typing import *
def f_gold(milestones: List[int]) -> int:
    mx, s = max(milestones), sum(milestones)
    rest = s - mx
    return rest * 2 + 1 if mx > rest + 1 else s
"-----------------"
test()

