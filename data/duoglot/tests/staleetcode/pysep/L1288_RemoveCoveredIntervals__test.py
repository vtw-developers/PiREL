from L1288_RemoveCoveredIntervals import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 4], [3, 6], [2, 8]]]
    # output: 2
    # EXPLANATION:  Interval [3,6] is covered by [2,8], therefore it is removed.
    ,
    # example 2
    [[[1, 4], [2, 3]]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
