from L0587_ErecttheFence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]]
    # output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
    ,
    # example 2
    [[[1, 2], [2, 2], [4, 2]]]
    # output: [[4,2],[2,2],[1,2]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
