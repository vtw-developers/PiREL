### countStudents 
from collections import Counter
from typing import *
def f_gold(students: List[int], sandwiches: List[int]) -> int:
    counter = Counter(students)
    for i, sandwich in enumerate(sandwiches):
        if counter[sandwich] == 0:
            return len(students) - i
        counter[sandwich] -= 1
    return 0