from L0473_MatchstickstoSquare import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 2, 2]]
    # output: true
    # EXPLANATION:  You can form a square with length 2, one side of the square came two sticks with length 1.
    ,
    # example 2
    [[3, 3, 3, 3, 4]]
    # output: false
    # EXPLANATION:  You cannot find a way to form a square with all the matchsticks.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
