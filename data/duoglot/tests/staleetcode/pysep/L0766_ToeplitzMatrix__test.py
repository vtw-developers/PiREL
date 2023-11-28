from L0766_ToeplitzMatrix import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]]
    # output: true
    # EXPLANATION:  In the above grid, the diagonals are: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]". In each diagonal all elements are the same, so the answer is True.
    ,
    # example 2
    [[[1, 2], [2, 2]]]
    # output: false
    # EXPLANATION:  The diagonal "[1, 2]" has different elements.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
