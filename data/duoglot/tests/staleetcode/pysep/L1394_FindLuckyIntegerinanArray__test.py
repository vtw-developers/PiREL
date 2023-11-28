from L1394_FindLuckyIntegerinanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 2, 3, 4]]
    # output: 2
    # EXPLANATION:  The only lucky number in the array is 2 because frequency[2] == 2.
    ,
    # example 2
    [[1, 2, 2, 3, 3, 3]]
    # output: 3
    # EXPLANATION:  1, 2 and 3 are all lucky numbers, return the largest of them.
    ,
    # example 3
    [[2, 2, 2, 3, 3]]
    # output: -1
    # EXPLANATION:  There are no lucky numbers in the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
