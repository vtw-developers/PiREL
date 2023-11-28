from L0561_ArrayPartitionI import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 4, 3, 2]]
    # output: 4
    # EXPLANATION:  All possible pairings (ignoring the ordering of elements) are: 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4 So the maximum possible sum is 4.
    ,
    # example 2
    [[6, 2, 6, 5, 1, 2]]
    # output: 9
    # EXPLANATION:  The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
