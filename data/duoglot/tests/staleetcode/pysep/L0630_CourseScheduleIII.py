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