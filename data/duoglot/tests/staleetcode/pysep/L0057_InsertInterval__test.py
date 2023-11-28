from L0057_InsertInterval import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 3], [6, 9]], [2, 5]]
    # output: [[1,5],[6,9]]
    ,
    # example 2
    [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]
    # output: [[1,2],[3,10],[12,16]]
    # EXPLANATION:  Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
