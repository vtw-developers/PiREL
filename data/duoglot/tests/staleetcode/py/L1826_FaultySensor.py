
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 4, 5], [2, 1, 3, 4]]
    # output: 1
    # EXPLANATION:  Sensor 2 has the correct values. The second data point from sensor 2 is dropped, and the last value of sensor 1 is replaced by a 5.
    ,
    # example 2
    [[2, 2, 2, 2, 2], [2, 2, 2, 2, 5]]
    # output: -1
    # EXPLANATION:  It is impossible to determine which sensor has a defect. Dropping the last value for either sensor could produce the output for the other sensor.
    ,
    # example 3
    [[2, 3, 2, 2, 3, 2], [2, 3, 2, 3, 2, 7]]
    # output: 2
    # EXPLANATION: Sensor 1 has the correct values. The fourth data point from sensor 1 is dropped, and the last value of sensor 1 is replaced by a 7.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### badSensor 
from typing import *
def f_gold(sensor1: List[int], sensor2: List[int]) -> int:
    i, n = 0, len(sensor1)
    while i < n - 1:
        if sensor1[i] != sensor2[i]:
            break
        i += 1
    while i < n - 1:
        if sensor1[i + 1] != sensor2[i]:
            return 1
        if sensor1[i] != sensor2[i + 1]:
            return 2
        i += 1
    return -1
"-----------------"
test()

