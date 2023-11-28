from L2162_MinimumCosttoSetCookingTime import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [1, 2, 1, 600]
    # output: 6
    # EXPLANATION:  The following are the possible ways to set the cooking time. - 1 0 0 0, interpreted as 10 minutes and 0 seconds.   The finger is already on digit 1, pushes 1 (with cost 1), moves to 0 (with cost 2), pushes 0 (with cost 1), pushes 0 (with cost 1), and pushes 0 (with cost 1).   The cost is: 1 + 2 + 1 + 1 + 1 = 6. This is the minimum cost. - 0 9 6 0, interpreted as 9 minutes and 60 seconds. That is also 600 seconds.   The finger moves to 0 (with cost 2), pushes 0 (with cost 1), moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).   The cost is: 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12. - 9 6 0, normalized as 0960 and interpreted as 9 minutes and 60 seconds.   The finger moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).   The cost is: 2 + 1 + 2 + 1 + 2 + 1 = 9.
    ,
    # example 2
    [0, 1, 2, 76]
    # output: 6
    # EXPLANATION:  The optimal way is to push two digits: 7 6, interpreted as 76 seconds. The finger moves to 7 (with cost 1), pushes 7 (with cost 2), moves to 6 (with cost 1), and pushes 6 (with cost 2). The total cost is: 1 + 2 + 1 + 2 = 6 Note other possible ways are 0076, 076, 0116, and 116, but none of them produces the minimum cost.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
