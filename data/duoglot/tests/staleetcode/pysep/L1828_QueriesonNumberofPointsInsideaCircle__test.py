from L1828_QueriesonNumberofPointsInsideaCircle import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]]
    # output: [3,2,2]
    # EXPLANATION: The points and circles are shown above. queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.
    ,
    # example 2
    [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]]
    # output: [2,3,2,4]
    # EXPLANATION: The points and circles are shown above. queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
