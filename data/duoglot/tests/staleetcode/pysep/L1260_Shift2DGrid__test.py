from L1260_Shift2DGrid import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1]
    # output: [[9,1,2],[3,4,5],[6,7,8]]
    ,
    # example 2
    [[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4]
    # output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    ,
    # example 3
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9]
    # output: [[1,2,3],[4,5,6],[7,8,9]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
