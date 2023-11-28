from L2318_NumberofDistinctRollSequences import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4]
    # output: 184
    # EXPLANATION:  Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc. Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6). (1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed). (1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3. There are a total of 184 distinct sequences possible, so we return 184.
    ,
    # example 2
    [2]
    # output: 22
    # EXPLANATION:  Some of the possible sequences are (1, 2), (2, 1), (3, 2). Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1. There are a total of 22 distinct sequences possible, so we return 22.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
