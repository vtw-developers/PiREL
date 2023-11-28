from L0004_MedianofTwoSortedArrays import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3], [2]]
    # output: 2.00000
    # EXPLANATION:  merged array = [1,2,3] and median is 2.
    ,
    # example 2
    [[1, 2], [3, 4]]
    # output: 2.50000
    # EXPLANATION:  merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
