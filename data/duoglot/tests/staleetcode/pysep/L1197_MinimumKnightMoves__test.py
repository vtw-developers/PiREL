from L1197_MinimumKnightMoves import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, 1]
    # output: 1
    # EXPLANATION: [0, 0]   [2, 1]
    ,
    # example 2
    [5, 5]
    # output: 4
    # EXPLANATION: [0, 0]   [2, 1]   [4, 2]   [3, 4]   [5, 5]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
