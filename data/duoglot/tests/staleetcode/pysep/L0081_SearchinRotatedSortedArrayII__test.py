from L0081_SearchinRotatedSortedArrayII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 5, 6, 0, 0, 1, 2], 0]
    # output: true
    ,
    # example 2
    [[2, 5, 6, 0, 0, 1, 2], 3]
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
