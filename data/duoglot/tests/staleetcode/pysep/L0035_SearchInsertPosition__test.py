from L0035_SearchInsertPosition import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 6], 5]
    # output: 2
    ,
    # example 2
    [[1, 3, 5, 6], 2]
    # output: 1
    ,
    # example 3
    [[1, 3, 5, 6], 7]
    # output: 4
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
