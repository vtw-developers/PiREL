from L0797_AllPathsFromSourcetoTarget import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2], [3], [3], []]]
    # output: [[0,1,3],[0,2,3]]
    # EXPLANATION:  There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
    ,
    # example 2
    [[[4, 3, 1], [3, 2, 4], [3], [4], []]]
    # output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
