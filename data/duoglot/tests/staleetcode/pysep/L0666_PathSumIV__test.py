from L0666_PathSumIV import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[113, 215, 221]]
    # output: 12
    # EXPLANATION:  The tree that the list represents is shown. The path sum is (3 + 5) + (3 + 1) = 12.
    ,
    # example 2
    [[113, 221]]
    # output: 4
    # EXPLANATION:  The tree that the list represents is shown.  The path sum is (3 + 1) = 4.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
