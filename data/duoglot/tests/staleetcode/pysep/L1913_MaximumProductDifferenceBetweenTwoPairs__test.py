from L1913_MaximumProductDifferenceBetweenTwoPairs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 6, 2, 7, 4]]
    # output: 34
    # EXPLANATION:  We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).  The product difference is (6 * 7) - (2 * 4) = 34.
    ,
    # example 2
    [[4, 2, 5, 9, 7, 4, 8]]
    # output: 64
    # EXPLANATION:  We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).  The product difference is (9 * 8) - (2 * 4) = 64.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
