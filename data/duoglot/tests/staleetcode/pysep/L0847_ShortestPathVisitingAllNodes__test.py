from L0847_ShortestPathVisitingAllNodes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [0], [0], [0]]]
    # output: 4
    # EXPLANATION:  One possible path is [1,0,2,0,3]
    ,
    # example 2
    [[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]]
    # output: 4
    # EXPLANATION:  One possible path is [0,1,4,2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
