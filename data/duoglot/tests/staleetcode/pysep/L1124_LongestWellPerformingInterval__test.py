from L1124_LongestWellPerformingInterval import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[9, 9, 6, 0, 6, 6, 9]]
    # output: 3
    # EXPLANATION: The longest well-performing interval is [9,9,6].
    ,
    # example 2
    [[6, 6, 6]]
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
