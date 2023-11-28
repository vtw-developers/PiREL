from L2139_MinimumMovestoReachTargetScore import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, 0]
    # output: 4
    # EXPLANATION:  Keep incrementing by 1 until you reach target.
    ,
    # example 2
    [19, 2]
    # output: 7
    # EXPLANATION:  Initially, x = 1 Increment 3 times so x = 4 Double once so x = 8 Increment once so x = 9 Double again so x = 18 Increment once so x = 19
    ,
    # example 3
    [10, 4]
    # output: 4
    # EXPLANATION: <b> </b>Initially, x = 1 Increment once so x = 2 Double once so x = 4 Increment once so x = 5 Double again so x = 10
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
