from L2291_MaximumProfitFromTradingStocks import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[5, 4, 6, 2, 3], [8, 5, 4, 3, 5], 10]
    # output: 6
    # EXPLANATION:  One possible way to maximize your profit is to: Buy the 0<sup>th</sup>, 3<sup>rd</sup>, and 4<sup>th</sup> stocks for a total of 5 + 2 + 3 = 10. Next year, sell all three stocks for a total of 8 + 3 + 5 = 16. The profit you made is 16 - 10 = 6. It can be shown that the maximum profit you can make is 6.
    ,
    # example 2
    [[2, 2, 5], [3, 4, 10], 6]
    # output: 5
    # EXPLANATION:  The only possible way to maximize your profit is to: Buy the 2<sup>nd</sup> stock, and make a profit of 10 - 5 = 5. It can be shown that the maximum profit you can make is 5.
    ,
    # example 3
    [[3, 3, 12], [0, 3, 15], 10]
    # output: 0
    # EXPLANATION:  One possible way to maximize your profit is to: Buy the 1<sup>st</sup> stock, and make a profit of 3 - 3 = 0. It can be shown that the maximum profit you can make is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
