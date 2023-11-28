from L1380_LuckyNumbersinaMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[3, 7, 8], [9, 11, 13], [15, 16, 17]]]
    # output: [15]
    # EXPLANATION:  15 is the only lucky number since it is the minimum in its row and the maximum in its column.
    ,
    # example 2
    [[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]]
    # output: [12]
    # EXPLANATION:  12 is the only lucky number since it is the minimum in its row and the maximum in its column.
    ,
    # example 3
    [[[7, 8], [1, 2]]]
    # output: [7]
    # EXPLANATION:  7 is the only lucky number since it is the minimum in its row and the maximum in its column.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
