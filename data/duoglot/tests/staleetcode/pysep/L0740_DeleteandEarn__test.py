from L0740_DeleteandEarn import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 4, 2]]
    # output: 6
    # EXPLANATION:  You can perform the following operations: - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2]. - Delete 2 to earn 2 points. nums = []. You earn a total of 6 points.
    ,
    # example 2
    [[2, 2, 3, 3, 3, 4]]
    # output: 9
    # EXPLANATION:  You can perform the following operations: - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3]. - Delete a 3 again to earn 3 points. nums = [3]. - Delete a 3 once more to earn 3 points. nums = []. You earn a total of 9 points.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
