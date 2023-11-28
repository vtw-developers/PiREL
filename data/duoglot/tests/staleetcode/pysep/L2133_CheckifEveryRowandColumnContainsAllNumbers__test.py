from L2133_CheckifEveryRowandColumnContainsAllNumbers import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [3, 1, 2], [2, 3, 1]]]
    # output: true
    # EXPLANATION:  In this case, n = 3, and every row and column contains the numbers 1, 2, and 3. Hence, we return true.
    ,
    # example 2
    [[[1, 1, 1], [1, 2, 3], [1, 2, 3]]]
    # output: false
    # EXPLANATION:  In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3. Hence, we return false.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
