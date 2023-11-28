from L1833_MaximumIceCreamBars import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 3, 2, 4, 1], 7]
    # output: 4
    # EXPLANATION: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
    ,
    # example 2
    [[10, 6, 8, 7, 7, 8], 5]
    # output: 0
    # EXPLANATION: The boy cannot afford any of the ice cream bars.
    ,
    # example 3
    [[1, 6, 3, 1, 2, 5], 20]
    # output: 6
    # EXPLANATION: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
