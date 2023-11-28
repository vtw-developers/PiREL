from L1423_MaximumPointsYouCanObtainfromCards import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4, 5, 6, 1], 3]
    # output: 12
    # EXPLANATION:  After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
    ,
    # example 2
    [[2, 2, 2], 2]
    # output: 4
    # EXPLANATION:  Regardless of which two cards you take, your score will always be 4.
    ,
    # example 3
    [[9, 7, 7, 9, 7, 7, 9], 7]
    # output: 55
    # EXPLANATION:  You have to take all the cards. Your score is the sum of points of all cards.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
