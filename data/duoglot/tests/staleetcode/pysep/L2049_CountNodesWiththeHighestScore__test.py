from L2049_CountNodesWiththeHighestScore import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-1, 2, 0, 2, 0]]
    # output: 3
    # EXPLANATION:  - The score of node 0 is: 3 * 1 = 3 - The score of node 1 is: 4 = 4 - The score of node 2 is: 1 * 1 * 2 = 2 - The score of node 3 is: 4 = 4 - The score of node 4 is: 4 = 4 The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
    ,
    # example 2
    [[-1, 2, 0]]
    # output: 2
    # EXPLANATION:  - The score of node 0 is: 2 = 2 - The score of node 1 is: 2 = 2 - The score of node 2 is: 1 * 1 = 1 The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
