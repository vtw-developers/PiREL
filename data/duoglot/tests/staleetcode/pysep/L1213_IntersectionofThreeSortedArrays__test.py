from L1213_IntersectionofThreeSortedArrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]]
    # output: [1,5]
    # EXPLANATION: Only 1 and 5 appeared in the three arrays.
    ,
    # example 2
    [[197, 418, 523, 876, 1356], [501, 880, 1593, 1710, 1870], [521, 682, 1337, 1395, 1764]]
    # output: []
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
