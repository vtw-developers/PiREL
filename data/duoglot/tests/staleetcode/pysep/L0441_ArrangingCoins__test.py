from L0441_ArrangingCoins import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [5]
    # output: 2
    # EXPLANATION:  Because the 3<sup>rd</sup> row is incomplete, we return 2.
    ,
    # example 2
    [8]
    # output: 3
    # EXPLANATION:  Because the 4<sup>th</sup> row is incomplete, we return 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
