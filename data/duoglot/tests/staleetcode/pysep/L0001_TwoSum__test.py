from L0001_TwoSum import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 7, 11, 15], 9]
    # output: [0,1]
    # EXPLANATION:  Because nums[0] + nums[1] == 9, we return [0, 1].
    ,
    # example 2
    [[3, 2, 4], 6]
    # output: [1,2]
    ,
    # example 3
    [[3, 3], 6]
    # output: [0,1]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
