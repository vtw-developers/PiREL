from L0279_PerfectSquares import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [12]
    # output: 3
    # EXPLANATION:  12 = 4 + 4 + 4.
    ,
    # example 2
    [13]
    # output: 2
    # EXPLANATION:  13 = 4 + 9.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
