from L0780_ReachingPoints import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 1, 3, 5]
    # output: true
    # EXPLANATION:  One series of moves that transforms the starting point to the target is: (1, 1) -> (1, 2) (1, 2) -> (3, 2) (3, 2) -> (3, 5)
    ,
    # example 2
    [1, 1, 2, 2]
    # output: false
    ,
    # example 3
    [1, 1, 1, 1]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
