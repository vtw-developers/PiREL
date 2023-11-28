from L1936_AddMinimumNumberofRungs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 10], 2]
    # output: 2
    # EXPLANATION: You currently cannot reach the last rung. Add rungs at heights 7 and 8 to climb this ladder.  The ladder will now have rungs at [1,3,5,<u>7</u>,<u>8</u>,10].
    ,
    # example 2
    [[3, 6, 8, 10], 3]
    # output: 0
    # EXPLANATION:  This ladder can be climbed without adding additional rungs.
    ,
    # example 3
    [[3, 4, 6, 7], 2]
    # output: 1
    # EXPLANATION:  You currently cannot reach the first rung from the ground. Add a rung at height 1 to climb this ladder. The ladder will now have rungs at [<u>1</u>,3,4,6,7].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
