from L0260_SingleNumberIII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 1, 3, 2, 5]]
    # output: [3,5]
    # EXPLANATION:  [5, 3] is also a valid answer.
    ,
    # example 2
    [[-1, 0]]
    # output: [-1,0]
    ,
    # example 3
    [[0, 1]]
    # output: [1,0]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
