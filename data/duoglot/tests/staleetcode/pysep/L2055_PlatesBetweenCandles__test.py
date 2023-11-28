from L2055_PlatesBetweenCandles import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["**|**|***|", [[2, 5], [5, 9]]]
    # output: [2,3]
    # EXPLANATION:  - queries[0] has two plates between candles. - queries[1] has three plates between candles.
    ,
    # example 2
    ["***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]]
    # output: [9,0,0,0,0]
    # EXPLANATION:  - queries[0] has nine plates between candles. - The other queries have zero plates between candles.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
