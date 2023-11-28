from L0376_WiggleSubsequence import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 7, 4, 9, 2, 5]]
    # output: 6
    # EXPLANATION:  The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
    ,
    # example 2
    [[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]]
    # output: 7
    # EXPLANATION:  There are several subsequences that achieve this length. One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
    ,
    # example 3
    [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
