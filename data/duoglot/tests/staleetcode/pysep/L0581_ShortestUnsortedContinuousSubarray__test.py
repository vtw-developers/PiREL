from L0581_ShortestUnsortedContinuousSubarray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 6, 4, 8, 10, 9, 15]]
    # output: 5
    # EXPLANATION:  You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: 0
    ,
    # example 3
    [[1]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
