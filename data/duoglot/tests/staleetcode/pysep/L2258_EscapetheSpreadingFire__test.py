from L2258_EscapetheSpreadingFire import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0]]]
    # output: 3
    # EXPLANATION:  The figure above shows the scenario where you stay in the initial position for 3 minutes. You will still be able to safely reach the safehouse. Staying for more than 3 minutes will not allow you to safely reach the safehouse.
    ,
    # example 2
    [[[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]]]
    # output: -1
    # EXPLANATION:  The figure above shows the scenario where you immediately move towards the safehouse. Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse. Thus, -1 is returned.
    ,
    # example 3
    [[[0, 0, 0], [2, 2, 0], [1, 2, 0]]]
    # output: 1000000000
    # EXPLANATION:  The figure above shows the initial grid. Notice that the fire is contained by walls and you will always be able to safely reach the safehouse. Thus, 10<sup>9</sup> is returned.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
