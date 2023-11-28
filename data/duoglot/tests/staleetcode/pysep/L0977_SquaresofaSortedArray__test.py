from L0977_SquaresofaSortedArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-4, -1, 0, 3, 10]]
    # output: [0,1,9,16,100]
    # EXPLANATION:  After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].
    ,
    # example 2
    [[-7, -3, 2, 3, 11]]
    # output: [4,9,9,49,121]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
