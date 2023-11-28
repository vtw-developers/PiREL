from L0852_PeakIndexinaMountainArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[0, 1, 0]]
    # output: 1
    ,
    # example 2
    [[0, 2, 1, 0]]
    # output: 1
    ,
    # example 3
    [[0, 10, 5, 2]]
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
