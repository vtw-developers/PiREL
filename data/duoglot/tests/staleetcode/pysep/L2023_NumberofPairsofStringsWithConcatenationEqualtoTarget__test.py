from L2023_NumberofPairsofStringsWithConcatenationEqualtoTarget import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [["777", "7", "77", "77"], "7777"]
    # output: 4
    # EXPLANATION:  Valid pairs are: - (0, 1): "777" + "7" - (1, 0): "7" + "777" - (2, 3): "77" + "77" - (3, 2): "77" + "77"
    ,
    # example 2
    [["123", "4", "12", "34"], "1234"]
    # output: 2
    # EXPLANATION:  Valid pairs are: - (0, 1): "123" + "4" - (2, 3): "12" + "34"
    ,
    # example 3
    [["1", "1", "1"], "11"]
    # output: 6
    # EXPLANATION:  Valid pairs are: - (0, 1): "1" + "1" - (1, 0): "1" + "1" - (0, 2): "1" + "1" - (2, 0): "1" + "1" - (1, 2): "1" + "1" - (2, 1): "1" + "1"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
