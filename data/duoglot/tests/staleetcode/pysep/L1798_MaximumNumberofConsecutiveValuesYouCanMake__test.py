from L1798_MaximumNumberofConsecutiveValuesYouCanMake import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3]]
    # output: 2
    # EXPLANATION: You can make the following values: - 0: take [] - 1: take [1] You can make 2 consecutive integer values starting from 0.
    ,
    # example 2
    [[1, 1, 1, 4]]
    # output: 8
    # EXPLANATION: You can make the following values: - 0: take [] - 1: take [1] - 2: take [1,1] - 3: take [1,1,1] - 4: take [4] - 5: take [4,1] - 6: take [4,1,1] - 7: take [4,1,1,1] You can make 8 consecutive integer values starting from 0.
    ,
    # example 3
    [[1, 4, 10, 3, 1]]
    # output: 20
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
