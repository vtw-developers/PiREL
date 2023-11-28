from L0435_NonoverlappingIntervals import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [2, 3], [3, 4], [1, 3]]]
    # output: 1
    # EXPLANATION:  [1,3] can be removed and the rest of the intervals are non-overlapping.
    ,
    # example 2
    [[[1, 2], [1, 2], [1, 2]]]
    # output: 2
    # EXPLANATION:  You need to remove two [1,2] to make the rest of the intervals non-overlapping.
    ,
    # example 3
    [[[1, 2], [2, 3]]]
    # output: 0
    # EXPLANATION:  You don't need to remove any of the intervals since they're already non-overlapping.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
