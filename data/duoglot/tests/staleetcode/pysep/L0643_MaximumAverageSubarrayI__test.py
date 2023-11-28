from L0643_MaximumAverageSubarrayI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 12, -5, -6, 50, 3], 4]
    # output: 12.75000
    # EXPLANATION:  Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    ,
    # example 2
    [[5], 1]
    # output: 5.00000
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
