from L0935_KnightDialer import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1]
    # output: 10
    # EXPLANATION:  We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
    ,
    # example 2
    [2]
    # output: 20
    # EXPLANATION:  All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
    ,
    # example 3
    [3131]
    # output: 136006598
    # EXPLANATION:  Please take care of the mod.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
