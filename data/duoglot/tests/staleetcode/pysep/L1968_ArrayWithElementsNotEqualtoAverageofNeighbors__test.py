from L1968_ArrayWithElementsNotEqualtoAverageofNeighbors import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5]]
    # output: [1,2,4,5,3]
    # EXPLANATION:  When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5. When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5. When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
    ,
    # example 2
    [[6, 2, 0, 9, 7]]
    # output: [9,7,6,2,0]
    # EXPLANATION:  When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5. When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5. When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
