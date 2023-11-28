from L1064_FixedPoint import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[-10, -5, 0, 3, 7]]
    # output: 3
    # EXPLANATION:  For the given array, <code>arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3</code>, thus the output is 3.
    ,
    # example 2
    [[0, 2, 5, 8, 17]]
    # output: 0
    # EXPLANATION:  <code>arr[0] = 0</code>, thus the output is 0.
    ,
    # example 3
    [[-10, -5, 3, 4, 7, 9]]
    # output: -1
    # EXPLANATION:  There is no such <code>i</code> that <code>arr[i] == i</code>, thus the output is -1.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
