from L1182_ShortestDistancetoTargetColor import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]]
    # output: [3,0,3]
    # EXPLANATION:  The nearest 3 from index 1 is at index 4 (3 steps away). The nearest 2 from index 2 is at index 2 itself (0 steps away). The nearest 1 from index 6 is at index 3 (3 steps away).
    ,
    # example 2
    [[1, 2], [[0, 3]]]
    # output: [-1]
    # EXPLANATION: There is no 3 in the array.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
