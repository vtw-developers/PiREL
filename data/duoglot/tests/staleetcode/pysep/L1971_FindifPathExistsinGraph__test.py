from L1971_FindifPathExistsinGraph import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[0, 1], [1, 2], [2, 0]], 0, 2]
    # output: true
    # EXPLANATION:  There are two paths from vertex 0 to vertex 2: - 0   1   2 - 0   2
    ,
    # example 2
    [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5]
    # output: false
    # EXPLANATION:  There is no path from vertex 0 to vertex 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
