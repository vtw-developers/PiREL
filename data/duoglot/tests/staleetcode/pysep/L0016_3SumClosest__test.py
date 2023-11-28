from L0016_3SumClosest import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 2, 1, -4], 1]
    # output: 2
    # EXPLANATION:  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    ,
    # example 2
    [[0, 0, 0], 1]
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
