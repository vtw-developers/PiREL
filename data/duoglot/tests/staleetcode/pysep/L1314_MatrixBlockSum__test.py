from L1314_MatrixBlockSum import f_gold

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
    # output: [[12,21,16],[27,45,33],[24,39,28]]
    ,
    # example 2
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2]
    # output: [[45,45,45],[45,45,45],[45,45,45]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
