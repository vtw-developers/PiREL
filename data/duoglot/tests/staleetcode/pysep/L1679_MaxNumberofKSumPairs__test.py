from L1679_MaxNumberofKSumPairs import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4], 5]
    # output: 2
    # EXPLANATION:  Starting with nums = [1,2,3,4]: - Remove numbers 1 and 4, then nums = [2,3] - Remove numbers 2 and 3, then nums = [] There are no more pairs that sum up to 5, hence a total of 2 operations.
    ,
    # example 2
    [[3, 1, 3, 4, 3], 6]
    # output: 1
    # EXPLANATION:  Starting with nums = [3,1,3,4,3]: - Remove the first two 3's, then nums = [1,4,3] There are no more pairs that sum up to 6, hence a total of 1 operation.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
