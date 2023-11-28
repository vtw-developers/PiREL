from L1377_FrogPositionAfterTSeconds import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4]
    # output: 0.16666666666666666
    # EXPLANATION:  The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after <strong>second 1</strong> and then jumping with 1/2 probability to vertex 4 after <strong>second 2</strong>. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666.
    ,
    # example 2
    [7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7]
    # output: 0.3333333333333333
    # EXPLANATION: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after <strong>second 1</strong>.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
