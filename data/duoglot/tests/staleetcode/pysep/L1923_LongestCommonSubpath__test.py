from L1923_LongestCommonSubpath import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5, [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]]
    # output: 2
    # EXPLANATION:  The longest common subpath is [2,3].
    ,
    # example 2
    [3, [[0], [1], [2]]]
    # output: 0
    # EXPLANATION:  There is no common subpath shared by the three paths.
    ,
    # example 3
    [5, [[0, 1, 2, 3, 4], [4, 3, 2, 1, 0]]]
    # output: 1
    # EXPLANATION:  The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
