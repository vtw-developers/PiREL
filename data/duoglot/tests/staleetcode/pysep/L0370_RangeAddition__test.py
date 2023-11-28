from L0370_RangeAddition import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]]
    # output: [-2,0,3,5,3]
    ,
    # example 2
    [10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]]]
    # output: [0,-4,2,2,2,4,4,-4,-4,-4]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
