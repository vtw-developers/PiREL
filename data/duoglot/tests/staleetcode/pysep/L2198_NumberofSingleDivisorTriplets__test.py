from L2198_NumberofSingleDivisorTriplets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 6, 7, 3, 2]]
    # output: 12
    # EXPLANATION: The triplets (0, 3, 4), (0, 4, 3), (3, 0, 4), (3, 4, 0), (4, 0, 3), and (4, 3, 0) have the values of [4, 3, 2] (or a permutation of [4, 3, 2]). 4 + 3 + 2 = 9 which is only divisible by 3, so all such triplets are single divisor triplets. The triplets (0, 2, 3), (0, 3, 2), (2, 0, 3), (2, 3, 0), (3, 0, 2), and (3, 2, 0) have the values of [4, 7, 3] (or a permutation of [4, 7, 3]). 4 + 7 + 3 = 14 which is only divisible by 7, so all such triplets are single divisor triplets. There are 12 single divisor triplets in total.
    ,
    # example 2
    [[1, 2, 2]]
    # output: 6
    # EXPLANATION:  The triplets (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), and (2, 1, 0) have the values of [1, 2, 2] (or a permutation of [1, 2, 2]). 1 + 2 + 2 = 5 which is only divisible by 1, so all such triplets are single divisor triplets. There are 6 single divisor triplets in total.
    ,
    # example 3
    [[1, 1, 1]]
    # output: 0
    # EXPLANATION:  There are no single divisor triplets. Note that (0, 1, 2) is not a single divisor triplet because nums[0] + nums[1] + nums[2] = 3 and 3 is divisible by nums[0], nums[1], and nums[2].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
