from L2176_CountEqualandDivisiblePairsinanArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[3, 1, 2, 2, 2, 1, 3], 2]
    # output: 4
    # EXPLANATION:  There are 4 pairs that meet all the requirements: - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2. - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2. - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2. - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
    ,
    # example 2
    [[1, 2, 3, 4], 1]
    # output: 0
    # EXPLANATION:  Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
