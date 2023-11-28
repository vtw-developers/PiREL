from L2293_MinMaxGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 2, 4, 8, 2, 2]]
    # output: 1
    # EXPLANATION:  The following arrays are the results of applying the algorithm repeatedly. First: nums = [1,5,4,2] Second: nums = [1,4] Third: nums = [1] 1 is the last remaining number, so we return 1.
    ,
    # example 2
    [[3]]
    # output: 3
    # EXPLANATION:  3 is already the last remaining number, so we return 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
