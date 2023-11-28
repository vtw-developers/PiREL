from L0219_ContainsDuplicateII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 1], 3]
    # output: true
    ,
    # example 2
    [[1, 0, 1, 1], 1]
    # output: true
    ,
    # example 3
    [[1, 2, 3, 1, 2, 3], 2]
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
