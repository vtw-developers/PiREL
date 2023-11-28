from L2322_MinimumScoreAfterRemovalsonaTree import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]]
    # output: 9
    # EXPLANATION:  The diagram above shows a way to make a pair of removals. - The 1<sup>st</sup> component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10. - The 2<sup>nd</sup> component has node [0] with value [1]. Its XOR value is 1 = 1. - The 3<sup>rd</sup> component has node [2] with value [5]. Its XOR value is 5 = 5. The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9. It can be shown that no other pair of removals will obtain a smaller score than 9.
    ,
    # example 2
    [[5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]]
    # output: 0
    # EXPLANATION:  The diagram above shows a way to make a pair of removals. - The 1<sup>st</sup> component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0. - The 2<sup>nd</sup> component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0. - The 3<sup>rd</sup> component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0. The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0. We cannot obtain a smaller score than 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
