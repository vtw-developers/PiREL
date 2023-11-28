from L0798_SmallestRotationwithHighestScore import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[2, 3, 1, 4, 0]]
    # output: 3
    # EXPLANATION:  Scores for each k are listed below:  k = 0,  nums = [2,3,1,4,0],    score 2 k = 1,  nums = [3,1,4,0,2],    score 3 k = 2,  nums = [1,4,0,2,3],    score 3 k = 3,  nums = [4,0,2,3,1],    score 4 k = 4,  nums = [0,2,3,1,4],    score 3 So we should choose k = 3, which has the highest score.
    ,
    # example 2
    [[1, 3, 0, 2, 4]]
    # output: 0
    # EXPLANATION:  nums will always have 3 points no matter how it shifts. So we will choose the smallest k, which is 0.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
