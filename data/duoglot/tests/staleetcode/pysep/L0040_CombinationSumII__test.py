from L0040_CombinationSumII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[10, 1, 2, 7, 6, 1, 5], 8]
    # output: [[1,1,6],[1,2,5],[1,7],[2,6]]
    ,
    # example 2
    [[2, 5, 2, 1, 2], 5]
    # output: [[1,2,2],[5]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
