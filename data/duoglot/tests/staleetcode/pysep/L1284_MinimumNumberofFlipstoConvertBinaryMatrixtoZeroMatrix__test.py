from L1284_MinimumNumberofFlipstoConvertBinaryMatrixtoZeroMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0], [0, 1]]]
    # output: 3
    # EXPLANATION:  One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
    ,
    # example 2
    [[[0]]]
    # output: 0
    # EXPLANATION:  Given matrix is a zero matrix. We do not need to change it.
    ,
    # example 3
    [[[1, 0, 0], [1, 0, 0]]]
    # output: -1
    # EXPLANATION:  Given matrix cannot be a zero matrix.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
