from L1742_MaximumNumberofBallsinaBox import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 10]
    # output: 2
    # EXPLANATION:  Box Number:  1 2 3 4 5 6 7 8 9 10 11 ... Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ... Box 1 has the most number of balls with 2 balls.
    ,
    # example 2
    [5, 15]
    # output: 2
    # EXPLANATION:  Box Number:  1 2 3 4 5 6 7 8 9 10 11 ... Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ... Boxes 5 and 6 have the most number of balls with 2 balls in each.
    ,
    # example 3
    [19, 28]
    # output: 2
    # EXPLANATION:  Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ... Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ... Box 10 has the most number of balls with 2 balls.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
