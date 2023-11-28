from L1826_FaultySensor import f_gold

##########
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

##########

test()
