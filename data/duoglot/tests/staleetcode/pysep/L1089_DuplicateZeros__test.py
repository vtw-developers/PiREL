from L1089_DuplicateZeros import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 0, 2, 3, 0, 4, 5, 0]]
    # output: [1,0,0,2,3,0,0,4]
    # EXPLANATION:  After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
    ,
    # example 2
    [[1, 2, 3]]
    # output: [1,2,3]
    # EXPLANATION:  After calling your function, the input array is modified to: [1,2,3]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
