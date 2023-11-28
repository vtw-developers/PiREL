from L0456_132Pattern import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: false
    # EXPLANATION:  There is no 132 pattern in the sequence.
    ,
    # example 2
    [[3, 1, 4, 2]]
    # output: true
    # EXPLANATION:  There is a 132 pattern in the sequence: [1, 4, 2].
    ,
    # example 3
    [[-1, 3, 2, 0]]
    # output: true
    # EXPLANATION:  There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
