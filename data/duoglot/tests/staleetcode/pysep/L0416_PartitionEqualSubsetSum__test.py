from L0416_PartitionEqualSubsetSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 5, 11, 5]]
    # output: true
    # EXPLANATION:  The array can be partitioned as [1, 5, 5] and [11].
    ,
    # example 2
    [[1, 2, 3, 5]]
    # output: false
    # EXPLANATION:  The array cannot be partitioned into equal sum subsets.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
