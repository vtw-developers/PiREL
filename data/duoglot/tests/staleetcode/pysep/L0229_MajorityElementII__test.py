from L0229_MajorityElementII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 2, 3]]
    # output: [3]
    ,
    # example 2
    [[1]]
    # output: [1]
    ,
    # example 3
    [[1, 2]]
    # output: [1,2]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
