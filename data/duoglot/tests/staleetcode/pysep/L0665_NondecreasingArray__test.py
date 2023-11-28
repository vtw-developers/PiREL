from L0665_NondecreasingArray import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[4, 2, 3]]
    # output: true
    # EXPLANATION:  You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
    ,
    # example 2
    [[4, 2, 1]]
    # output: false
    # EXPLANATION:  You can't get a non-decreasing array by modify at most one element.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
