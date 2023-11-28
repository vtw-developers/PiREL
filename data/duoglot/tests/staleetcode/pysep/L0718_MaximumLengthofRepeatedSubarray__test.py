from L0718_MaximumLengthofRepeatedSubarray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 2, 1], [3, 2, 1, 4, 7]]
    # output: 3
    # EXPLANATION:  The repeated subarray with maximum length is [3,2,1].
    ,
    # example 2
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    # output: 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
