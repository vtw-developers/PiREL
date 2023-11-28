from L1361_ValidateBinaryTreeNodes import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [4, [1, -1, 3, -1], [2, -1, -1, -1]]
    # output: true
    ,
    # example 2
    [4, [1, -1, 3, -1], [2, 3, -1, -1]]
    # output: false
    ,
    # example 3
    [2, [1, 0], [-1, -1]]
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
