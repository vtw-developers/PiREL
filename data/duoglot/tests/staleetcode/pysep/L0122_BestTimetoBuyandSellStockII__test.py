from L0122_BestTimetoBuyandSellStockII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[7, 1, 5, 3, 6, 4]]
    # output: 7
    # EXPLANATION:  Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.
    ,
    # example 2
    [[1, 2, 3, 4, 5]]
    # output: 4
    # EXPLANATION:  Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.
    ,
    # example 3
    [[7, 6, 4, 3, 1]]
    # output: 0
    # EXPLANATION:  There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
