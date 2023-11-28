from L1895_LargestMagicSquare import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]]
    # output: 3
    # EXPLANATION:  The largest magic square has a size of 3. Every row sum, column sum, and diagonal sum of this magic square is equal to 12. - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12 - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12 - Diagonal sums: 5+4+3 = 6+4+2 = 12
    ,
    # example 2
    [[[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]]
    # output: 2
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
