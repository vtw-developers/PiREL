from L1523_CountOddNumbersinanIntervalRange import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 7]
    # output: 3
    # EXPLANATION: The odd numbers between 3 and 7 are [3,5,7].
    ,
    # example 2
    [8, 10]
    # output: 1
    # EXPLANATION: The odd numbers between 8 and 10 are [9].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
