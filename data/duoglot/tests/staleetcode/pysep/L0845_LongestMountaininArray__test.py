from L0845_LongestMountaininArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 4, 7, 3, 2, 5]]
    # output: 5
    # EXPLANATION:  The largest mountain is [1,4,7,3,2] which has length 5.
    ,
    # example 2
    [[2, 2, 2]]
    # output: 0
    # EXPLANATION:  There is no mountain.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
