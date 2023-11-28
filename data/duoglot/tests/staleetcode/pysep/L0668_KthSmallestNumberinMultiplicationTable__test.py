from L0668_KthSmallestNumberinMultiplicationTable import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 3, 5]
    # output: 3
    # EXPLANATION:  The 5<sup>th</sup> smallest number is 3.
    ,
    # example 2
    [2, 3, 6]
    # output: 6
    # EXPLANATION:  The 6<sup>th</sup> smallest number is 6.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
