from L1243_ArrayTransformation import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[6, 2, 3, 4]]
    # output: [6,3,3,4]
    # EXPLANATION:  On the first day, the array is changed from [6,2,3,4] to [6,3,3,4]. No more operations can be done to this array.
    ,
    # example 2
    [[1, 6, 3, 4, 3, 5]]
    # output: [1,4,4,4,4,5]
    # EXPLANATION:  On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5]. On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5]. No more operations can be done to this array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
