from L1129_ShortestPathwithAlternatingColors import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1], [1, 2]], []]
    # output: [0,1,-1]
    ,
    # example 2
    [3, [[0, 1]], [[2, 1]]]
    # output: [0,1,-1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
