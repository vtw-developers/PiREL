from L2206_DivideArrayIntoEqualPairs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 3, 2, 2, 2]]
    # output: true
    # EXPLANATION:   There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs. If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
    ,
    # example 2
    [[1, 2, 3, 4]]
    # output: false
    # EXPLANATION:   There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
