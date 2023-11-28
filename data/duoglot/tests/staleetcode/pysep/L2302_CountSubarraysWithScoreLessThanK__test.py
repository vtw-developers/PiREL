from L2302_CountSubarraysWithScoreLessThanK import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 1, 4, 3, 5], 10]
    # output: 6
    # EXPLANATION:  The 6 subarrays having scores less than 10 are: - [2] with score 2 * 1 = 2. - [1] with score 1 * 1 = 1. - [4] with score 4 * 1 = 4. - [3] with score 3 * 1 = 3.  - [5] with score 5 * 1 = 5. - [2,1] with score (2 + 1) * 2 = 6. Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
    ,
    # example 2
    [[1, 1, 1], 5]
    # output: 5
    # EXPLANATION:  Every subarray except [1,1,1] has a score less than 5. [1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5. Thus, there are 5 subarrays having scores less than 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
