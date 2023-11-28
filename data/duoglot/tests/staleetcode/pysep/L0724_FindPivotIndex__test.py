from L0724_FindPivotIndex import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 7, 3, 6, 5, 6]]
    # output: 3
    # EXPLANATION:  The pivot index is 3. Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 Right sum = nums[4] + nums[5] = 5 + 6 = 11
    ,
    # example 2
    [[1, 2, 3]]
    # output: -1
    # EXPLANATION:  There is no index that satisfies the conditions in the problem statement.
    ,
    # example 3
    [[2, 1, -1]]
    # output: 0
    # EXPLANATION:  The pivot index is 0. Left sum = 0 (no elements to the left of index 0) Right sum = nums[1] + nums[2] = 1 + -1 = 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
