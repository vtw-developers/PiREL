from L1711_CountGoodMeals import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 5, 7, 9]]
    # output: 4
    # EXPLANATION: The good meals are (1,3), (1,7), (3,5) and, (7,9). Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
    ,
    # example 2
    [[1, 1, 1, 3, 3, 3, 7]]
    # output: 15
    # EXPLANATION: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
