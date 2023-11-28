from L0565_ArrayNesting import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 0, 3, 1, 6, 2]]
    # output: 4
    # EXPLANATION:   nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2. One of the longest sets s[k]: s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
    ,
    # example 2
    [[0, 1, 2]]
    # output: 1
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
