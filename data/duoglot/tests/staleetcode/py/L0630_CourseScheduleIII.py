
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]]
    # output: 3
    # EXPLANATION:   There are totally 4 courses, but you can take 3 courses at most: First, take the 1<sup>st</sup> course, it costs 100 days so you will finish it on the 100<sup>th</sup> day, and ready to take the next course on the 101<sup>st</sup> day. Second, take the 3<sup>rd</sup> course, it costs 1000 days so you will finish it on the 1100<sup>th</sup> day, and ready to take the next course on the 1101<sup>st</sup> day.  Third, take the 2<sup>nd</sup> course, it costs 200 days so you will finish it on the 1300<sup>th</sup> day.  The 4<sup>th</sup> course cannot be taken now, since you will finish it on the 3300<sup>th</sup> day, which exceeds the closed date.
    ,
    # example 2
    [[[1, 2]]]
    # output: 1
    ,
    # example 3
    [[[3, 2], [4, 3]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### scheduleCourse 
from heapq import heapify, heappush, heappop
from typing import *
def f_gold(courses: List[List[int]]) -> int:
    courses.sort(key=lambda x: x[1])
    pq = []
    s = 0
    for d, e in courses:
        heappush(pq, -d)
        s += d
        if s > e:
            s += heappop(pq)
    return len(pq)
"-----------------"
test()

