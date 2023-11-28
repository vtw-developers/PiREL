from L1345_JumpGameIV import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]]
    # output: 3
    # EXPLANATION:  You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
    ,
    # example 2
    [[7]]
    # output: 0
    # EXPLANATION:  Start index is the last index. You do not need to jump.
    ,
    # example 3
    [[7, 6, 9, 6, 9, 6, 9, 7]]
    # output: 1
    # EXPLANATION:  You can jump directly from index 0 to index 7 which is last index of the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
