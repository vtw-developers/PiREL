from L0886_PossibleBipartition import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [[1, 2], [1, 3], [2, 4]]]
    # output: true
    # EXPLANATION:  group1 [1,4] and group2 [2,3].
    ,
    # example 2
    [3, [[1, 2], [1, 3], [2, 3]]]
    # output: false
    ,
    # example 3
    [5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]]
    # output: false
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
