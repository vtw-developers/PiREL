from L0056_MergeIntervals import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3], [2, 6], [8, 10], [15, 18]]]
    # output: [[1,6],[8,10],[15,18]]
    # EXPLANATION:  Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    ,
    # example 2
    [[[1, 4], [4, 5]]]
    # output: [[1,5]]
    # EXPLANATION:  Intervals [1,4] and [4,5] are considered overlapping.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
