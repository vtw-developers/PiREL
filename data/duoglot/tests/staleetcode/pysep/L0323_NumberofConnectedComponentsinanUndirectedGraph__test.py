from L0323_NumberofConnectedComponentsinanUndirectedGraph import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1], [1, 2], [3, 4]]]
    # output: 2
    ,
    # example 2
    [5, [[0, 1], [1, 2], [2, 3], [3, 4]]]
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
