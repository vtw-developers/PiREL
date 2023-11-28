from L0698_PartitiontoKEqualSumSubsets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 3, 2, 3, 5, 2, 1], 4]
    # output: true
    # EXPLANATION:  It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
    ,
    # example 2
    [[1, 2, 3, 4], 3]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
