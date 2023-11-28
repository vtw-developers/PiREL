from L1135_ConnectingCitiesWithMinimumCost import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]]
    # output: 6
    # EXPLANATION:  Choosing any 2 edges will connect all cities so we choose the minimum 2.
    ,
    # example 2
    [4, [[1, 2, 3], [3, 4, 4]]]
    # output: -1
    # EXPLANATION:  There is no way to connect all cities even if all edges are used.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
