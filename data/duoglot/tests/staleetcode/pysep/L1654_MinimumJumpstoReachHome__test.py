from L1654_MinimumJumpstoReachHome import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[14, 4, 18, 1, 15], 3, 15, 9]
    # output: 3
    # EXPLANATION:  3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
    ,
    # example 2
    [[8, 3, 16, 6, 12, 20], 15, 13, 11]
    # output: -1
    ,
    # example 3
    [[1, 6, 2, 14, 5, 17, 4], 16, 9, 7]
    # output: 2
    # EXPLANATION:  One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
