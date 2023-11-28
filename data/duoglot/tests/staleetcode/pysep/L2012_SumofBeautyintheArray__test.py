from L2012_SumofBeautyintheArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3]]
    # output: 2
    # EXPLANATION:  For each index i in the range 1 <= i <= 1: - The beauty of nums[1] equals 2.
    ,
    # example 2
    [[2, 4, 6, 4]]
    # output: 1
    # EXPLANATION:  For each index i in the range 1 <= i <= 2: - The beauty of nums[1] equals 1. - The beauty of nums[2] equals 0.
    ,
    # example 3
    [[3, 2, 1]]
    # output: 0
    # EXPLANATION:  For each index i in the range 1 <= i <= 1: - The beauty of nums[1] equals 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
