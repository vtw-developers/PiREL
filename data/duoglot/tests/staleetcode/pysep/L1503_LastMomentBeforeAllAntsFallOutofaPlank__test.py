from L1503_LastMomentBeforeAllAntsFallOutofaPlank import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [4, 3], [0, 1]]
    # output: 4
    # EXPLANATION:  In the image above: -The ant at index 0 is named A and going to the right. -The ant at index 1 is named B and going to the right. -The ant at index 3 is named C and going to the left. -The ant at index 4 is named D and going to the left. The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).
    ,
    # example 2
    [7, [], [0, 1, 2, 3, 4, 5, 6, 7]]
    # output: 7
    # EXPLANATION:  All ants are going to the right, the ant at index 0 needs 7 seconds to fall.
    ,
    # example 3
    [7, [0, 1, 2, 3, 4, 5, 6, 7], []]
    # output: 7
    # EXPLANATION:  All ants are going to the left, the ant at index 7 needs 7 seconds to fall.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
