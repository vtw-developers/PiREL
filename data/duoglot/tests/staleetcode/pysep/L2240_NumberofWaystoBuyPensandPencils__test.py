from L2240_NumberofWaystoBuyPensandPencils import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [20, 10, 5]
    # output: 9
    # EXPLANATION:  The price of a pen is 10 and the price of a pencil is 5. - If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils. - If you buy 1 pen, you can buy 0, 1, or 2 pencils. - If you buy 2 pens, you cannot buy any pencils. The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.
    ,
    # example 2
    [5, 10, 10]
    # output: 1
    # EXPLANATION:  The price of both pens and pencils are 10, which cost more than total, so you cannot buy any writing utensils. Therefore, there is only 1 way: buy 0 pens and 0 pencils.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
