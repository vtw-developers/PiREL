from L0054_SpiralMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    # output: [1,2,3,6,9,8,7,4,5]
    ,
    # example 2
    [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    # output: [1,2,3,4,8,12,11,10,9,5,6,7]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
