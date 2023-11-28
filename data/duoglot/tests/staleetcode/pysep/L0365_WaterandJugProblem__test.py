from L0365_WaterandJugProblem import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [3, 5, 4]
    # output: true
    # EXPLANATION:  The famous <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg&ab_channel=notnek01" target="_blank">Die Hard</a> example
    ,
    # example 2
    [2, 6, 5]
    # output: false
    ,
    # example 3
    [1, 2, 3]
    # output: true
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
