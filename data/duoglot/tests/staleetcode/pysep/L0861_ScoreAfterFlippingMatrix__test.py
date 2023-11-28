from L0861_ScoreAfterFlippingMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]]
    # output: 39
    # EXPLANATION:  0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
    ,
    # example 2
    [[[0]]]
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
