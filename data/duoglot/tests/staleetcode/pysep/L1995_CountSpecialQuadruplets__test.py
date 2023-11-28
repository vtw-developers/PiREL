from L1995_CountSpecialQuadruplets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 6]]
    # output: 1
    # EXPLANATION:  The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
    ,
    # example 2
    [[3, 3, 6, 4, 5]]
    # output: 0
    # EXPLANATION:  There are no such quadruplets in [3,3,6,4,5].
    ,
    # example 3
    [[1, 1, 1, 3, 5]]
    # output: 4
    # EXPLANATION:  The 4 quadruplets that satisfy the requirement are: - (0, 1, 2, 3): 1 + 1 + 1 == 3 - (0, 1, 3, 4): 1 + 1 + 3 == 5 - (0, 2, 3, 4): 1 + 1 + 3 == 5 - (1, 2, 3, 4): 1 + 1 + 3 == 5
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
