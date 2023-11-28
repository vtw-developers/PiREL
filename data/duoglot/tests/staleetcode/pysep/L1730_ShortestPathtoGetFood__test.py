from L1730_ShortestPathtoGetFood import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["X", "X", "X", "X", "X", "X"], ["X", "*", "O", "O", "O", "X"], ["X", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X"]]]
    # output: 3
    # EXPLANATION:  It takes 3 steps to reach the food.
    ,
    # example 2
    [[["X", "X", "X", "X", "X"], ["X", "*", "X", "O", "X"], ["X", "O", "X", "#", "X"], ["X", "X", "X", "X", "X"]]]
    # output: -1
    # EXPLANATION:  It is not possible to reach the food.
    ,
    # example 3
    [[["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "*", "O", "X", "O", "#", "O", "X"], ["X", "O", "O", "X", "O", "O", "X", "X"], ["X", "O", "O", "O", "O", "#", "O", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]]
    # output: 6
    # EXPLANATION:  There can be multiple food cells. It only takes 6 steps to reach the bottom food.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
