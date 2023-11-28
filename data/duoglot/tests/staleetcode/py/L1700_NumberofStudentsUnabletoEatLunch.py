
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 0, 0], [0, 1, 0, 1]]
    # output: 0<strong>
    # EXPLANATION: </strong> - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1]. - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1]. - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1]. - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0]. - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1]. - Front student leaves the top sandwich and returns to the end of the line making students = [0,1]. - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1]. - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = []. Hence all students are able to eat.
    ,
    # example 2
    [[1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]]
    # output: 3
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
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
"-----------------"
test()

