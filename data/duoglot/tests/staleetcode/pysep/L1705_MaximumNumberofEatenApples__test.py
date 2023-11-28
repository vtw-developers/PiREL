from L1705_MaximumNumberofEatenApples import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 5, 2], [3, 2, 1, 4, 2]]
    # output: 7
    # EXPLANATION:  You can eat 7 apples: - On the first day, you eat an apple that grew on the first day. - On the second day, you eat an apple that grew on the second day. - On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot. - On the fourth to the seventh days, you eat apples that grew on the fourth day.
    ,
    # example 2
    [[3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]]
    # output: 5
    # EXPLANATION:  You can eat 5 apples: - On the first to the third day you eat apples that grew on the first day. - Do nothing on the fouth and fifth days. - On the sixth and seventh days you eat apples that grew on the sixth day.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
