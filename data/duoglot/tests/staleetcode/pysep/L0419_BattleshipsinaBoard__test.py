from L0419_BattleshipsinaBoard import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]]
    # output: 2
    ,
    # example 2
    [[["."]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
