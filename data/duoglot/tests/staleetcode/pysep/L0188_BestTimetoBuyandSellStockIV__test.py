from L0188_BestTimetoBuyandSellStockIV import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [2, [2, 4, 1]]
    # output: 2
    # EXPLANATION:  Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    ,
    # example 2
    [2, [3, 2, 6, 5, 0, 3]]
    # output: 7
    # EXPLANATION:  Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
