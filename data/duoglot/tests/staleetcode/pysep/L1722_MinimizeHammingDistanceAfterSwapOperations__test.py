from L1722_MinimizeHammingDistanceAfterSwapOperations import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]]
    # output: 1
    # EXPLANATION:  source can be transformed the following way: - Swap indices 0 and 1: source = [<u>2</u>,<u>1</u>,3,4] - Swap indices 2 and 3: source = [2,1,<u>4</u>,<u>3</u>] The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
    ,
    # example 2
    [[1, 2, 3, 4], [1, 3, 2, 4], []]
    # output: 2
    # EXPLANATION:  There are no allowed swaps. The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
    ,
    # example 3
    [[5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]]]
    # output: 0
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
