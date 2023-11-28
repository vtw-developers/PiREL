from L0765_CouplesHoldingHands import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 2, 1, 3]]
    # output: 1
    # EXPLANATION:  We only need to swap the second (row[1]) and third (row[2]) person.
    ,
    # example 2
    [[3, 2, 0, 1]]
    # output: 0
    # EXPLANATION:  All couples are already seated side by side.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
