from L2011_FinalValueofVariableAfterPerformingOperations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["--X", "X++", "X++"]]
    # output: 1
    # EXPLANATION:  The operations are performed as follows: Initially, X = 0. --X: X is decremented by 1, X =  0 - 1 = -1. X++: X is incremented by 1, X = -1 + 1 =  0. X++: X is incremented by 1, X =  0 + 1 =  1.
    ,
    # example 2
    [["++X", "++X", "X++"]]
    # output: 3
    # EXPLANATION: The operations are performed as follows: Initially, X = 0. ++X: X is incremented by 1, X = 0 + 1 = 1. ++X: X is incremented by 1, X = 1 + 1 = 2. X++: X is incremented by 1, X = 2 + 1 = 3.
    ,
    # example 3
    [["X++", "++X", "--X", "X--"]]
    # output: 0
    # EXPLANATION:  The operations are performed as follows: Initially, X = 0. X++: X is incremented by 1, X = 0 + 1 = 1. ++X: X is incremented by 1, X = 1 + 1 = 2. --X: X is decremented by 1, X = 2 - 1 = 1. X--: X is decremented by 1, X = 1 - 1 = 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
