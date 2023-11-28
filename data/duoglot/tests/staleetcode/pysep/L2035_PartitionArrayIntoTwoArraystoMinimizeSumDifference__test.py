from L2035_PartitionArrayIntoTwoArraystoMinimizeSumDifference import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 9, 7, 3]]
    # output: 2
    # EXPLANATION:  One optimal partition is: [3,9] and [7,3]. The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
    ,
    # example 2
    [[-36, 36]]
    # output: 72
    # EXPLANATION:  One optimal partition is: [-36] and [36]. The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
    ,
    # example 3
    [[2, -1, 0, 4, -2, -9]]
    # output: 0
    # EXPLANATION:  One optimal partition is: [2,4,-9] and [-1,0,-2]. The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
